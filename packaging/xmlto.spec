#
# spec file for package xmlto
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%if 0%{?suse_version} < 1030
%define dist_has_fdupes 0
%else
%define dist_has_fdupes 1
%endif

# support SLE 11
%if !0%{?make_install:1}
%define make_install %{makeinstall}
%endif

Name:           xmlto
Version:        0.0.25
Release:        0
License:        GPL-2.0+
Summary:        Tool for Converting XML Files to Various Formats
Url:            https://fedorahosted.org/xmlto/
Group:          Productivity/Publishing/XML
Source0:        https://fedorahosted.org/releases/x/m/xmlto/%{name}-%{version}.tar.bz2
Source10:       %{name}-README.SuSE
Patch0:         xmlto-nonvoid.patch
Patch1:         xmlto-overflow.patch
Patch3:         xmlto-xsltopts.patch
Patch4:         xmlto-codecleanup.patch
Patch5:         xmlto-lynx-empty-file.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  flex
BuildRequires:  libxslt
BuildRequires:  sgml-skel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if %{dist_has_fdupes}
BuildRequires:  fdupes
%endif

# We rely entirely on the DocBook XSL stylesheets!
Requires:       docbook-xsl-stylesheets >= 1.56.0
Requires:       docbook_4
Requires:       xsltproc
# For full functionality, we need passivetex.
Recommends:     texlive-xmltex >= 2007

%description
This is a package for converting XML files to various formats using XSL
stylesheets.  As a processor it depends on xsltproc and as a formatter
for print output it makes use of passivetex.

%prep
%setup -q
%patch0
%patch1
%patch3
%patch4
%patch5
cp %{SOURCE10} README.SuSE
rm -f xmlif/xmlif.c

%build
%configure
make %{?_smp_mflags}

%check
make check

%install
%make_install
! mkdir %{buildroot}%{_datadir}/xmlto/xsl
%if %{dist_has_fdupes}
%{fdupes '%{buildroot}%{_datadir}/xmlto'}
%endif

%files
%defattr(-,root,root)
%doc README.SuSE
%doc COPYING
%doc AUTHORS README ChangeLog FAQ THANKS NEWS
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xmlto

%changelog
