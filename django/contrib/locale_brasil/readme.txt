
Este repositório do Django contém uma correção para o locale pt_BR
da glibc, fazendo com que a ordem alfabética seja a correta, de acordo
com o bom senso, e com a norma da ABNT que está no PDF neste diretório.

Para testar esse locale, de forma não permanente, no terminal, faça o seguinte:

set LOCPATH=/caminho/para/o/django/conf/locale
set NLSPATH=/caminho/para/o/django/conf/locale
set LC_ALL=pt_BR.UTF-8
sort testa_ordem_nomes.txt

O resultado dessa ordem alfabética foi debatido aqui:

https://sourceware.org/bugzilla/show_bug.cgi?id=3405


