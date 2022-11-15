Name:		texlive-abntexto
Version:	64694
Release:	1
Summary:	LaTeX class for formatting academic papers in ABNT standards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/abntexto
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abntexto.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abntexto.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX class created for Brazilian students to
facilitate the use of standards from the Associacao Brasileira
de Normas Tecnicas (ABNT) in academic works like TCCs,
dissertations, theses.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/abntexto
%doc %{_texmfdistdir}/doc/latex/abntexto

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
