Pywrt
======

#### Esse pacote permite o desenvolvedor traduzir frases, ou docoumentos PDF, de um idioma para o outro.   
&nbsp;

## Instalação
    
    "pip install Pywrt"
&nbsp;

## Guia para traduzir texto:

'''
import Pywrt

a = Pywrt ( )

a.tranlate_text( "seu_texto" , "idioma_alvo" )
'''  
&nbsp;  
&nbsp;

## Guia para traduzir documento:

'''
import Pywrt

a = Pywrt ( )

a.tranlate_document( "caminho_do_documento" , "idioma_alvo" )
'''  
&nbsp;  
&nbsp;

## Obs:
Os documentos traduzidos são salvos na pasta "saida" que será criada no mesmo local da execução.