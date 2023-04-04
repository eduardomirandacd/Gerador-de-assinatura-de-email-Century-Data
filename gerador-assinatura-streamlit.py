import re
import streamlit as st

st.title("Gerador de assinatura email Century Data")

nome_sobrenome = st.text_input('Insira o seu nome e sobrenome', 'Nome Sobrenome')
email = st.text_input('Insira o seu email', 'nome.sobrenome@centurydata.com.br')
telefone_original = st.text_input('Insira o seu telefone de acordo com o formato', '(11) 987654321')
telefone_apenas_numeros = ''.join(re.findall(r'\d+', telefone_original))

html_string = "\
<iframe style='width:100%' srcdoc= \"\
	<html> \
	   <head> \
	      <meta charset='utf-8' /> \
	      <meta http-equiv='X-UA-Compatible' content='IE=edge' /> \
	      <meta name='viewport' content='width=device-width, initial-scale=1' /> \
	      <title>Century Data BR email signature</title> \
	      <link href='css/bootstrap.min.css' rel='stylesheet' /> \
	      <style type='text/css'> \
	         body, \
	         p, \
	         td, \
	         span { a \
	         font-family: sans-serif !important; \
	         font-size: 11px !important; \
	         color: #303030 !important; \
	         line-height: 120% !important; \
	         } \
	         a, \
	         a:hover, \
	         a:visited, \
	         a:active, \
	         .ii a[href], \
	         .ii a[href]:hover, \
	         .gt a, \
	         a:link, \
	         a:any-link { \
	         color: #1f58a8 !important; \
	         text-decoration: none !important; \
	         } \
	         .blue-bold { \
	         color: #0d3978 !important; \
	         font-size: 13px !important; \
	         font-weight: bold !important; \
	         } \
	         .regular-text { \
	         color: #303030 !important; \
	         font-weight: normal !important; \
	         text-decoration: none !important; \
	         } \
	         .bold-text { \
	         color: #303030 !important; \
	         font-weight: bold !important; \
	         text-decoration: none !important; \
	         } \
	      </style> \
	   </head> \
	   <body style='border-width: 0'> \
	      <div style='width: 500px;'> \
	         <table style='width: 100%; border: 0px none !important; vertical-align: top; margin-bottom: 0px;'> \
	            <tr> \
	               <td style='width: 120; border-right: solid 1px #f0f0f0; padding: 0px !important; padding-right: 8px !important; vertical-align: center;'> \
	                  <a href='http://www.centurydata.com.br/' target='_blank'> \
	                  <img src='https://centurydata.s3.amazonaws.com/assinatura-email/v2/centurydata-130px.png' alt='Century Data BR' style='width: 130px; height: auto; border: none 0px !important;' /> \
	                  </a> \
	               </td> \
	               <td style='padding-left: 15px; vertical-align: top;'> \
	                  <table style='width: 100%; border: 0px none !important; vertical-align: top; margin-bottom: 0px;'> \
	                     <tr> \
	                        <span class='blue-bold'><label id='labelNome'>{nomesobrenome}</label></span> \
	                        <br /> \
	                        <label id='labelCargo' class='regular-text'>{email}</label> \
	                        <br /> \
	                        <br /> \
	                        <span class='blue-bold'>tel </span> \
	                        <span class='regular-text'><a href='tel:+55{telefoneapenasnumeros}' style='color: #303030 !important; text-decoration: none !important;'>+55 {telefoneoriginal}</a></span> \
	                        <br /> \
	                     </tr> \
	                     <tr> \
	                        <div > \
	                           <table > \
	                              <tbody > \
	                                 <tr> \
	                                    <td style='border-right: 4px solid #FFFFFF;'> \
	                                       <a title='Whatsapp' href='https://wa.me/+55{telefoneapenasnumeros}' target='_blank'> \
	                                       <img src='https://centurydata.s3.amazonaws.com/assinatura-email/v2/whatsapp.png' alt='Whatsapp' style='width: 25px; height: auto; padding-right: 2px;'' /> \
	                                       </a> \
	                                    </td> \
	                                    <td style='border-right: 4px solid #FFFFFF;'> \
	                                       <a href='https://www.linkedin.com/company/centurydata-br/' target='_blank'> \
	                                       <img src='https://centurydata.s3.amazonaws.com/assinatura-email/v2/linkedin.png' alt='Century Data BR Linkedin' style='width: 25px; height: auto; padding-right: 2px;' />\
	                                       </a> \
	                                    </td> \
	                                    <td style='border-right: 4px solid #FFFFFF;'> \
	                                       <a href='http://www.centurydata.com.br/' target='_blank'> \
	                                       <img src='https://centurydata.s3.amazonaws.com/assinatura-email/v2/internet.png' alt='Century Data BR website' style='width: 25px; height: auto; padding-right: 2px;' /> \
	                                       </a> \
	                                    </td> \
	                                 </tr> \
	                              </tbody> \
	                           </table> \
	                        </div> \
	                     </tr> \
	                  </table> \
	               </td> \
	            </tr> \
	         </table> \
	      </div> \
	   </body> \
	</html>\"> \
</iframe>"

html_string = html_string.replace("{nomesobrenome}", nome_sobrenome).replace("{email}", email).replace("{telefoneoriginal}", telefone_original).replace("{telefoneapenasnumeros}", telefone_apenas_numeros)

st.text("")
st.markdown(html_string, unsafe_allow_html=True)
