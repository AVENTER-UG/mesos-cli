with import <nixpkgs> {};

stdenv.mkDerivation {
name = "python-env";

buildInputs = [
    python314
    python314Packages.pip
    python314Packages.virtualenv
];

SOURCE_DATE_EPOCH = 315532800;
PROJDIR = "/tmp/python-env";

shellHook = ''
    echo "Using ${python314.name}"
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib"
    
    [ ! -d '$PROJDIR/python-dev' ] && virtualenv $PROJDIR && echo "SETUP python-dev: DONE"

    source $PROJDIR/bin/activate
    pip install avmesos
    make install-dev

    '';
}
