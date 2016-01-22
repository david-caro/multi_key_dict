%define short_name multi_key_dict
%define name python-%{short_name}
%define version 2.0.3
%define unmangled_version %{version}
%define release 1%{?dist}

Summary: UNKNOWN
Name: %{name}
Version: %{version}
Release: %{release}
License: Unknown
Source0: %{short_name}-%{unmangled_version}.tar.gz
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Url: https://github.com/formiaczek/multi_key_dict
BuildRequires: python
BuildRequires: python-setuptools

%description
 multiple key dictionary for Python

%prep
%setup -n %{short_name}-%{unmangled_version} -n %{short_name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
