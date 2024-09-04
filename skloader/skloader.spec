Name:           skloader
Version:        0.0.1
Release:        1%{?dist}
Summary:        Secure kernel bootloader

License:        GPLv2
Source0:        skloader-0.0.1.tar.gz

# Need to avoid debug until Makefile is fixed to use normal build vars
%global debug_package %{nil}

%description
This package contains the bootloader for LVBS's secure kernel.

%prep
%autosetup

%build
%make_build

%install
install -D -m 0755 -t %{buildroot}%{_libexecdir}/lvbs skloader.bin

%files
%{_libexecdir}/lvbs/skloader.bin

%changelog
* Thu Aug 29 05:45:51 UTC 2024 Angelina Vu <angelinavu@microsoft.com>
- Initial spec file for skloader 
