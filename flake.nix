{
  description = "Environment for this program";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: 
  let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in
  {
    packages.x86_64-linux.python3 = pkgs.python312Full;
    packages.x86_64-linux.python-vlc = pkgs.python312Packages.python-vlc;
    packages.x86_64-linux.default = self.packages.x86_64-linux.python3;

    devShells.x86_64-linux.default = pkgs.mkShell {
      buildInputs = [
        self.packages.x86_64-linux.python3
        self.packages.x86_64-linux.python-vlc
      ];
      shellHook = "python3 ./main.py";
    };
  };
}
