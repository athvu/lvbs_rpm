Name:           lvbs-secure
Version:        0.0.1
Release:        1%{?dist}
Summary:        LVBS secure kernel

License:        GPLv2
Source0:        lvbs-secure-0.0.1.tar.gz     

%description
LVBS's secure linux kernel to run in VTL1.

%prep
%autosetup

%build
%make_build mshv_sk_defconfig
%make_build vmlinux
objcopy -O binary -R .note -R .comment -S vmlinux vmlinux.bin

%install
install -D -m 0755 -t %{buildroot}%{_libexecdir}/lvbs vmlinux.bin

%files
%{_libexecdir}/lvbs/vmlinux.bin

%changelog
* Thu Aug 29 07:19:39 UTC 2024 Angelina Vu <angelinavu@microsoft.com>
- Initial spec file for LVBS secure kernel
