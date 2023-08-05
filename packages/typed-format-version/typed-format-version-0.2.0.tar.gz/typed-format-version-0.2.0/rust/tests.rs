//! Some tests for the typed-format-version library.
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

#![allow(clippy::panic_in_result_fn)]

use std::collections::HashMap;
use std::error::Error;
use std::fs;
use std::path::Path;

use serde::Deserialize;
use serde_json::Value as JsonValue;
use serde_yaml::Value as YamlValue;
use toml::Value as TomlValue;
use tracing::info;
use tracing_test::traced_test;

#[derive(Debug, Deserialize)]
struct CorrectDataJson {
    raw: JsonValue,
    version: super::Version,
}

#[derive(Debug, Deserialize)]
struct CorrectTopJson {
    correct: HashMap<String, CorrectDataJson>,
}

#[derive(Debug, Deserialize)]
struct CorrectDataYaml {
    raw: YamlValue,
    version: super::Version,
}

#[derive(Debug, Deserialize)]
struct CorrectTopYaml {
    correct: HashMap<String, CorrectDataYaml>,
}

#[derive(Debug, Deserialize)]
struct CorrectDataToml {
    raw: TomlValue,
    version: super::Version,
}

#[derive(Debug, Deserialize)]
struct CorrectTopToml {
    correct: HashMap<String, CorrectDataToml>,
}

#[derive(Debug, Deserialize)]
struct WrongTopJson {
    wrong: HashMap<String, JsonValue>,
}

#[derive(Debug, Deserialize)]
struct WrongTopYaml {
    wrong: HashMap<String, YamlValue>,
}

#[derive(Debug, Deserialize)]
struct WrongTopToml {
    wrong: HashMap<String, TomlValue>,
}

#[test]
#[traced_test]
fn test_good() -> Result<(), Box<dyn Error>> {
    let tpath = Path::new("test_data/correct.toml").canonicalize()?;
    let contents_toml = fs::read_to_string(&tpath)?;
    let value_toml: TomlValue = toml::from_str(&contents_toml)?;
    let fver = super::get_version_from_value(value_toml.clone())?;
    info!(?fver);
    assert_eq!((fver.major(), fver.minor()), (1, 0));

    let tdata_toml: CorrectTopToml = toml::from_str(&contents_toml)?;
    for (name, tcase) in tdata_toml.correct {
        info!(tag = "toml", name, ?tcase.version);

        let raw = toml::to_string(&tcase.raw)?;
        let ver_str = super::get_version_from_str(&raw, toml::from_str)?;
        info!(tag = "toml", ?ver_str);
        assert_eq!(ver_str, tcase.version);

        let ver_val = super::get_version_from_value(tcase.raw)?;
        info!(tag = "toml", ?ver_val);
        assert_eq!(ver_val, tcase.version);
    }

    let contents = serde_json::to_string(&value_toml)?;
    let tdata_json: CorrectTopJson = serde_json::from_str(&contents)?;
    for (name, tcase) in tdata_json.correct {
        info!(tag = "json", name, ?tcase.version);

        let raw = serde_json::to_string(&tcase.raw)?;
        let ver_str = super::get_version_from_str(&raw, serde_json::from_str)?;
        info!(tag = "json", ?ver_str);
        assert_eq!(ver_str, tcase.version);

        let ver_val = super::get_version_from_value(tcase.raw)?;
        info!(tag = "json", ?ver_val);
        assert_eq!(ver_val, tcase.version);
    }

    let tdata_yaml: CorrectTopYaml = serde_yaml::from_str(&contents)?;
    for (name, tcase) in tdata_yaml.correct {
        info!(tag = "yaml", name, ?tcase.version);

        let raw = serde_yaml::to_string(&tcase.raw)?;
        let ver_str = super::get_version_from_str(&raw, serde_yaml::from_str)?;
        info!(tag = "yaml", ?ver_str);
        assert_eq!(ver_str, tcase.version);

        let ver_val = super::get_version_from_value(tcase.raw)?;
        info!(tag = "yaml", ?ver_val);
        assert_eq!(ver_val, tcase.version);
    }

    Ok(())
}

#[test]
#[traced_test]
fn test_bad() -> Result<(), Box<dyn Error>> {
    let tpath = Path::new("test_data/wrong.toml").canonicalize()?;
    let contents_toml = fs::read_to_string(&tpath)?;
    let value_toml: TomlValue = toml::from_str(&contents_toml)?;
    let fver = super::get_version_from_value(value_toml.clone())?;
    assert_eq!((fver.major(), fver.minor()), (1, 0));

    let tdata_toml: WrongTopToml = toml::from_str(&contents_toml)?;
    for (name, tcase) in tdata_toml.wrong {
        info!(tag = "toml", name);

        let raw = toml::to_string(&tcase)?;
        let res_str = super::get_version_from_str(&raw, toml::from_str);
        info!(tag = "toml", ?res_str);
        res_str.unwrap_err();

        let res_val = super::get_version_from_value(tcase);
        info!(tag = "toml", ?res_val);
        res_val.unwrap_err();
    }

    let contents = serde_json::to_string(&value_toml)?;
    let tdata_json: WrongTopJson = serde_json::from_str(&contents)?;
    for (name, tcase) in tdata_json.wrong {
        info!(tag = "json", name);

        let raw = serde_json::to_string(&tcase)?;
        let res_str = super::get_version_from_str(&raw, serde_json::from_str);
        info!(tag = "json", ?res_str);
        res_str.unwrap_err();

        let res_val = super::get_version_from_value(tcase);
        info!(tag = "json", ?res_val);
        res_val.unwrap_err();
    }

    let tdata_yaml: WrongTopYaml = serde_yaml::from_str(&contents)?;
    for (name, tcase) in tdata_yaml.wrong {
        info!(tag = "yaml", name);

        let raw = serde_yaml::to_string(&tcase)?;
        let res_str = super::get_version_from_str(&raw, serde_yaml::from_str);
        info!(tag = "yaml", ?res_str);
        res_str.unwrap_err();

        let res_val = super::get_version_from_value(tcase);
        info!(tag = "yaml", ?res_val);
        res_val.unwrap_err();
    }

    Ok(())
}
