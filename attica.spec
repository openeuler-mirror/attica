Name:           attica
Version:        0.4.2
Release:        21
Summary:        Implementation of the Open Collaboration Services API

License:        Artistic-2.0 and LGPLv2+
URL:            http://www.kde.org
Source0:        http://download.kde.org/stable/attica/attica-%{version}.tar.bz2

patch1: 0001-Add-auto-generated-files-to-.gitignore.patch
patch2: fix-clang.patch

BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(QtNetwork) >= 4.7

%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.


%prep
%setup -q
%patch1 -p1
%patch2 -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} .. \
  -DQT4_BUILD:BOOL=ON
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
# verify pkg-config sanitry/version
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libattica)" = "%{version}"


%ldconfig_scriptlets

%files
%doc AUTHORS README
%doc ChangeLog
%license COPYING
%{_libdir}/libattica.so.0.4*

%files devel
%{_includedir}/attica/
%{_libdir}/libattica.so
%{_libdir}/pkgconfig/libattica.pc


%changelog
* Tue Jun 20 2023 yoo <sunyuechi@iscas.ac.cn> - 0.4.2-21
- fix clang build error

* Tue Apr 26 2022 tanyulong <tanyulong@kylinos.cn> - 0.4.2-20
- modify license warning

* Wed Dec 22 2021 tanyulong <tanyulong@kylinos.cn> - 0.4.2-19
- Add auto generated files to .gitignore

* Mon Dec 12 2020 huanghaitao <huanghaitao8@huawei.com> - 0.4.2-18
- Remove the release suffix

* Thu Jul 23 2020 wangmian<wangmian@kylinos.cn> - 0.4.2-17
- Init attica project
