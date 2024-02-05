# BIO727P-Team-Deepin

## HT 31 Jan 2024 - set up LFS for repository 
 
(base) harrytowner@192 ~ % brew install git-lfs
Running `brew update --auto-update`...
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
deadfinder               icloudpd                 libspelling              nowplaying-cli           rsyncy                   senpai                   tfautomv                 zigmod
git-grab                 libnsgif                 limesuite                openjph                  scnlib                   terrapin-scanner         tomlplusplus
==> New Casks
bitbox                            cleanupbuddy                      easydevo                          lyricsfinder                      shadow-bot                        ttu-base-suite
bugdom2                           domzilla-caffeine                 insomnium                         nightshade                        theiaide

You have 1 outdated formula installed.

==> Downloading https://ghcr.io/v2/homebrew/core/git-lfs/manifests/3.4.1
##################################################################################################################################################################################################### 100.0%
==> Fetching git-lfs
==> Downloading https://ghcr.io/v2/homebrew/core/git-lfs/blobs/sha256:63461c3fbf6ddab9d90c8c6dcb51748a68c4446f222709b970dd688dd78a77f6
##################################################################################################################################################################################################### 100.0%
==> Pouring git-lfs--3.4.1.arm64_sonoma.bottle.tar.gz
==> Caveats
Update your git config to finish installation:

  # Update global git config
  $ git lfs install

  # Update system git config
  $ git lfs install --system
==> Summary
🍺  /opt/homebrew/Cellar/git-lfs/3.4.1: 78 files, 13.1MB
==> Running `brew cleanup git-lfs`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
(base) harrytowner@192 ~ % git lfs install
Git LFS initialized.
(base) harrytowner@192 ~ % git lfs version
git-lfs/3.4.1 (GitHub; darwin arm64; go 1.21.5)
(base) harrytowner@192 BIO727P - Bioinformatics Software Development Group Project - 2024 % git clone git@github.com:Towner101/BIO727P-Team-Deepin.git
Cloning into 'BIO727P-Team-Deepin'...
Enter passphrase for key '/Users/harrytowner/.ssh/id_rsa': 
remote: Enumerating objects: 27, done.
remote: Counting objects: 100% (27/27), done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 27 (delta 3), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (27/27), 40.43 KiB | 475.00 KiB/s, done.
Resolving deltas: 100% (3/3), done.

## Steps to set up LFS on others computers 

*Instal git LFS
*Run 'git lfs install'
*Clone the repository 
*Pull LFS Tracked Files with 'git lfs pull'
*Work within the repository on local computer 
*Push changes made on local computer to remote repository with 'git push' 
