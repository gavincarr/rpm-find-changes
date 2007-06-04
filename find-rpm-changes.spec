
Name: find-rpm-changes
Summary: Report files not belonging to an rpm, or that have changed from their rpm versions
Version: 0.1
Release: 1%{?org_tag}
Source0: %{name}-%{version}.tar.gz
License: GPL
URL: http://www.openfusion.com.au/labs/
Group: Applications/File
Packager: Gavin Carr <gavin@openfusion.com.au>
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch
BuildRequires: perl

%description
find-rpm-changes is a script to report files within a tree whose contents 
have changed from their rpm versions, or which are not owned by any rpm.
It is intended to help identify candidate files for backup.

%prep
%setup
  
%build 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%install
mkdir -p %{buildroot}%{_bindir} 
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/cron.d
mkdir -p %{buildroot}/var/cache/%{name}
  
install -m0755 bin/find-rpm-changes %{buildroot}%{_bindir}

install -m0644 etc/exclude* %{buildroot}%{_sysconfigdir}/%{name}

install -m0644 etc/%{name}.cron %{buildroot}%{_sysconfigdir}/cron.d/%[name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/cron.d/*
%dir %{buildroot}/var/cache/%{name}

%changelog

* Tue Jun 05 2007 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial spec file.

