//! typed-format-version: load format.version.{major,minor} from a structured file.
//!
//! This library tries to parse a format.version "section" in some raw data that
//! may have been loaded from a configuration file, and determines whether that
//! section contains valid "major" and "minor" integer values. The caller can
//! then choose the correct schema to validate the loaded data against, e.g. by
//! using a `serde`-derived library with the correct top-level dataclass definition.
//!
//! The most commonly used function will probably be `get_version_from_str()`:
//! it takes a string and a deserialization function and returns a `Version` object
//! with a `major` and `minor` integer attributes, if the data contained a valid
//! "format" element with a "version" element within it.
//!
//! ```rust
//! // This would usually be read from a file.
//! let contents = r#"{"format": {"version": {"major": 1, "minor": 3}}, "data": ["hello"]}"#;
//!
//! let fver = typed_format_version::get_version_from_str(&contents, serde_json::from_str)
//!    .expect("Could not get the data format version");
//! if (fver.major(), fver.minor()) != (1, 3) {
//!     panic!("Unexpected data format version {}.{}", fver.major(), fver.minor());
//! }
//! // Load the data as usual using e.g. serde_json::from_str().
//! ```
//!
//! Examining the returned version also allows loading data in different formats
//! using e.g. deserialization of different top-level structures and then performing
//! some kind of data migration to the preferred one.
/*
 * Copyright (c) 2022  Peter Pentchev <roam@ringlet.net>
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#![deny(missing_docs)]

use std::error::Error;
use std::fmt::{Display, Error as FmtError, Formatter};

use quick_error::quick_error;
use serde::{Deserialize, Deserializer};

#[cfg(test)]
mod tests;

quick_error! {
    /// An error that occurred during the processing of the format data.
    #[derive(Debug)]
    #[non_exhaustive]
    pub enum LoadError {
        /// Could not parse the format.version.{major,minor} structure.
        Format(msg: String) {
            display("Could not parse format.version: {}", msg)
        }
    }
}

/// A trivial representation of a major.minor version string.
pub type VersionTuple = (u32, u32);

impl From<&Version> for VersionTuple {
    #[inline]
    fn from(ver: &Version) -> Self {
        (ver.major, ver.minor)
    }
}

/// The representation of a major.minor version string.
#[derive(Debug, Deserialize, PartialEq, Eq)]
pub struct Version {
    /// The major version number.
    major: u32,

    /// The minor version number.
    minor: u32,
}

impl Version {
    /// Construct a new version object.
    #[must_use]
    #[inline]
    pub const fn new(major: u32, minor: u32) -> Self {
        Self { major, minor }
    }

    /// Get the major version number.
    #[allow(clippy::must_use_candidate)]
    #[inline]
    pub const fn major(&self) -> u32 {
        self.major
    }

    /// Get the minor version number.
    #[allow(clippy::must_use_candidate)]
    #[inline]
    pub const fn minor(&self) -> u32 {
        self.minor
    }

    /// Return the major.minor information as a tuple.
    #[allow(clippy::must_use_candidate)]
    #[inline]
    pub const fn as_version_tuple(&self) -> VersionTuple {
        (self.major, self.minor)
    }
}

impl Display for Version {
    #[inline]
    fn fmt(&self, writer: &mut Formatter<'_>) -> Result<(), FmtError> {
        write!(writer, "{}.{}", self.major, self.minor)
    }
}

/// The metadata about the file format, currently the version information.
#[derive(Debug, Deserialize)]
pub struct Format {
    /// The file format version information.
    version: Version,
}

impl Format {
    /// Get the version information.
    #[allow(clippy::must_use_candidate)]
    #[inline]
    pub const fn version(&self) -> &Version {
        &self.version
    }
}

/// The top-level element containing a "format" structure.
#[derive(Debug, Deserialize)]
pub struct FormatOnlyTop {
    /// The metadata about the file format.
    format: Format,
}

/// Parse the format section from a string.
///
/// # Errors
/// [`LoadError::Format`] if the string cannot be parsed into
/// a structure containing a valid "format" substructure.
#[inline]
pub fn get_format_from_str<'contents, 'data, E, F>(
    contents: &'contents str,
    from_str_fn: F,
) -> Result<Format, LoadError>
where
    'contents: 'data,
    E: Error + 'static,
    F: Fn(&'data str) -> Result<FormatOnlyTop, E>,
{
    Ok(from_str_fn(contents)
        .map_err(|err| LoadError::Format(err.to_string()))?
        .format)
}

/// Parse format.version from a string.
///
/// # Errors
/// Any error returned by the [`get_format_from_str()`] function.
#[inline]
pub fn get_version_from_str<'contents, 'data, E, F>(
    contents: &'contents str,
    from_str_fn: F,
) -> Result<Version, LoadError>
where
    'contents: 'data,
    E: Error + 'static,
    F: Fn(&'data str) -> Result<FormatOnlyTop, E>,
{
    Ok(get_format_from_str(contents, from_str_fn)?.version)
}

/// Parse the format section from an arbitrary deserializable value.
/// The `value` parameter may be a struct similar to `serde_json::Value`,
/// `serde_yaml::Value`, or `toml::Value`.
///
/// # Errors
/// [`LoadError::Format`] if the value cannot be parsed into
/// a structure containing a valid "format" substructure.
#[inline]
pub fn get_format_from_value<'de, V: Deserializer<'de>>(value: V) -> Result<Format, LoadError> {
    let ftop: FormatOnlyTop =
        FormatOnlyTop::deserialize(value).map_err(|err| LoadError::Format(err.to_string()))?;
    Ok(ftop.format)
}

/// Parse format.version from an arbitrary value.
/// The `value` parameter may be a struct similar to `serde_json::Value`,
/// `serde_yaml::Value`, or `toml::Value`.
///
/// # Errors
/// Any error returned by the [`get_format_from_value()`] function.
#[inline]
pub fn get_version_from_value<'de, V: Deserializer<'de>>(value: V) -> Result<Version, LoadError> {
    Ok(get_format_from_value(value)?.version)
}
