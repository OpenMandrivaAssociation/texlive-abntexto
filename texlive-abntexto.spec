%global tl_name abntexto
%global tl_revision 78949

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	LaTeX class for formatting academic papers in ABNT standards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abntexto
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abntexto.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abntexto.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX class created for Brazilian students to facilitate the
use of standards from the Associacao Brasileira de Normas Tecnicas
(ABNT) in academic works like TCCs, dissertations, theses.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/abntexto
%dir %{_datadir}/texmf-dist/tex/latex/abntexto
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/README.md
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto-birds.jpg
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto-exemplo.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto-exemplo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto-exemplo.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto-onehalf-tex.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto-onehalf-word.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto-screenshot.png
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntexto/abntexto.tex
%{_datadir}/texmf-dist/tex/latex/abntexto/abntexto-3-2-1-beta.cls
%{_datadir}/texmf-dist/tex/latex/abntexto/abntexto.cls
