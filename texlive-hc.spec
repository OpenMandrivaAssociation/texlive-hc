Name:		texlive-hc
Version:	20080420
Release:	1
Summary:	Replacement for the LaTeX classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hc
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A set of replacements for the default LaTeX classes, based upon
the Koma-Script bundle and the seminar class. Includes hcart,
hcreport, hcletter, and hcslides.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/hc/hc-de.bst
%{_texmfdistdir}/bibtex/bst/hc/hc-en.bst
%{_texmfdistdir}/tex/latex/hc/german.hld
%{_texmfdistdir}/tex/latex/hc/hcart.cls
%{_texmfdistdir}/tex/latex/hc/hcletter.cls
%{_texmfdistdir}/tex/latex/hc/hcreport.cls
%{_texmfdistdir}/tex/latex/hc/hcslides.cls
%doc %{_texmfdistdir}/doc/latex/hc/COPYING
%doc %{_texmfdistdir}/doc/latex/hc/FILES
%doc %{_texmfdistdir}/doc/latex/hc/README
%doc %{_texmfdistdir}/doc/latex/hc/hc.ps
#- source
%doc %{_texmfdistdir}/source/latex/hc/hc.dtx
%doc %{_texmfdistdir}/source/latex/hc/hc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
