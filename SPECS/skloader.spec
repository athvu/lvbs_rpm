Name:           skloader
Version:        0.0.1
Release:        1%{?dist}
Summary:        Secure kernel bootloader 

License:        GPLv2 
Source0:        skloader-0.0.1.tar.gz

%description
This package contains the bootloader for LVBS's secure kernel.

%prep
%autosetup


%build
make


%changelog
* Thu Aug 29 05:45:51 UTC 2024 Angelina Vu <angelinavu@microsoft.com>
- Initial spec file for skloader 
