# vim: sw=4:ts=4:et

%define selinux_policyver 34.21-1

Name:   xonadm_selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module for xonadm

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		http://HOSTNAME
Source0:	xonadm.pp
Source1:	xonadm.if
Source2:	xonadm_selinux.8
Source3:	xonadm_u

Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for xonadm.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/xonadm_selinux.8
install -d %{buildroot}/etc/selinux/targeted/contexts/users/
install -m 644 %{SOURCE3} %{buildroot}/etc/selinux/targeted/contexts/users/xonadm_u

%post
semodule -n -i %{_datadir}/selinux/packages/xonadm.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    
    /usr/sbin/semanage user -a -R xonadm_r xonadm_u
fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r xonadm
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       
       /usr/sbin/semanage user -d xonadm_u
    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/xonadm.pp
%{_datadir}/selinux/devel/include/contrib/xonadm.if
%{_mandir}/man8/xonadm_selinux.8.*
/etc/selinux/targeted/contexts/users/xonadm_u

%changelog
* Sun Oct 24 2021 YOUR NAME <YOUR@EMAILADDRESS> 1.0-1
- Initial version

