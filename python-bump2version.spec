# Created by pyp2rpm-3.3.5
%global pypi_name bump2version

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1
Summary:        Version-bump your software with a single command!
Group:          Development/Python
License:        MIT
URL:            https://github.com/c4urself/bump2version
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 bump2version[![image]( [![image]( [![image]( [![Travis]( [![AppVeyor](
NOTEThis is a maintained fork of the excellent [bumpversion project](

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

#%check
#%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE.rst
%doc README.md
%{_bindir}/bump2version
%{_bindir}/bumpversion
%{python3_sitelib}/bumpversion
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

