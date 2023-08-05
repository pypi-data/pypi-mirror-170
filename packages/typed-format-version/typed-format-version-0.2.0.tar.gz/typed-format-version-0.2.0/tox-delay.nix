{ pkgs ? import (fetchTarball
  "https://github.com/ppentchev/nixpkgs/archive/roam-tox-tomli.tar.gz") { }
, py-ver ? 310 }:
let
  python-name = "python${toString py-ver}";
  python = builtins.getAttr python-name pkgs;
  python-with-tox = python.withPackages (p: with p; [ tox ]);
in pkgs.mkShell {
  buildInputs = [ python-with-tox ];
  shellHook = ''
    set -e
    TOX_SKIP_ENV=unit_tests tox -p all
    tox -p all -e unit-tests
    exit
  '';
}
