
Name: rpm-find-changes
Summary: Report files not belonging to an rpm, or that have changed from their rpm versions
Version: 0.4.1
Release: 1%{?org_tag}
Source0: %{name}-%{version}.tar.gz
License: GPL
URL: http://www.openfusion.com.au/labs/
Group: Applications/File
Packager: Gavin Carr <gavin@openfusion.com.au>
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch
BuildRequires: perl, /usr/bin/pod2man
Requires: perl(RPM2)

%description
rpm-find-changes is a script to report files within a tree whose contents 
have changed from their rpm versions, or which are not owned by any rpm.
It is intended to help identify candidate files for backup.

%prep
%setup
  
%build 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%install
mkdir -p %{buildroot}%{_bindir} 
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/cron.d
mkdir -p %{buildroot}/var/cache/%{name}
  
install -m0755 bin/rpm-find-changes %{buildroot}%{_bindir}

pod2man --section=1 -r "rpm-find-changes $RPM_PACKAGE_VERSION" bin/rpm-find-changes > %{buildroot}%{_mandir}/man1/rpm-find-changes.1

cp etc/exclude* %{buildroot}%{_sysconfdir}/%{name}

cp etc/%{name}.cron %{buildroot}%{_sysconfdir}/cron.d/%{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/cron.d/*
%dir /var/cache/%{name}

%changelog
* Tue Dec 29 2009 Gavin Carr <gavin@openfusion.com.au> 0.4.1-1
- Tweak use of binmode for old versions of IO::File.

* Thu Dec 04 2009 Gavin Carr <gavin@openfusion.com.au> 0.4-1
- Replace rpm -V verification with manual checksum verification using Digest::MD5.
- Refactor old bodgy code into subroutines.

* Thu Dec 03 2009 Gavin Carr <gavin@openfusion.com.au> 0.3.4-1
- Remove skipping of empty files - now record everything.
- Escape '.' chars when turning excludes into regexes.
- Add version control directories to default exclude-etc.

* Fri Jun 20 2008 Gavin Carr <gavin@openfusion.com.au> 0.3.3-1
- Exclude core files in default exclude-etc.

* Fri Jun 20 2008 Gavin Carr <gavin@openfusion.com.au> 0.3.2-1
- Tweak default exclude-etc to not exclude /etc/rc.d/init.d.
- Add rpm-find-changes.1 man page from pod.

* Fri Oct 05 2007 Gavin Carr <gavin@openfusion.com.au> 0.3.1-1
- Fix bad bug introduced in 0.3 with orphans not working with RPM2.

* Sat Sep 15 2007 Gavin Carr <gavin@openfusion.com.au> 0.3-1
- Remove RPM2 requirement, to get working on RHEL2 with ancient rpm.

* Wed Aug 01 2007 Gavin Carr <gavin@openfusion.com.au> 0.2.3-1
- Add /etc/cups/certs to default exclude-etc.

* Thu Jun 21 2007 Gavin Carr <gavin@openfusion.com.au> 0.2.2-1
- Add a couple of daemontools excludes to default exclude-etc.

* Tue Jun 05 2007 Gavin Carr <gavin@openfusion.com.au> 0.2.1-1
- Set O_TRUNC on file output.

* Tue Jun 05 2007 Gavin Carr <gavin@openfusion.com.au> 0.2-1
- Turn on Getopt::Long case insensitivity and bundling.

* Tue Jun 05 2007 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial spec file.

