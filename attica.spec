
Name:           attica
Version:        0.4.2
Release:        17%{?dist}
Summary:        Implementation of the Open Collaboration Services API

License:        LGPLv2+
URL:            http://www.kde.org
Source0:        http://download.kde.org/stable/attica/attica-%{version}.tar.bz2

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
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
