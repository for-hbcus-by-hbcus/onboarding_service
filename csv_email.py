import smtplib, csv, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes


emailSubject= "Complete your account to For HBCUs, By HBCUs Presented by The NFL";
sender = "hello@forhbcusbyhbcus.com";
password = "BattleOfTheBrains123"


msg = EmailMessage()
#body = MIMEText(bodyText)
msg['Subject'] = emailSubject
msg['From'] = sender  

img_content_id = make_msgid(domain='Users/rasonirvin/Desktop/logo.png') # update path to match needs

with open('students.csv', newline='') as csvfile:
    recipients = list(csv.reader(csvfile))

#for loop
for recipient in recipients:
    msg['To'] = recipient[0]

    msg.set_content('This is a plain text body.')

    msg.add_alternative("""\
    <p>&nbsp;</p>
<table style="width: 600px;" border="0" cellspacing="0" cellpadding="0" bgcolor="#ff0000">
   <tbody>
      <tr>
         <td>
            <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
               <tbody>
                  <tr>
                     <td>
                        <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0" align="center" bgcolor="#fff">
                           <tbody>
                              <tr>
                                 <td align="center">
                                    <div>
                                       <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0" bgcolor="#fff">
                                          <tbody>
                                             <tr>
                                                <td align="center"><img class="CToWUd" src="https://mail.google.com/mail/u/0?ui=2&amp;ik=6830fcdd05&amp;attid=0.1&amp;permmsgid=msg-a:r-7765606156952027011&amp;th=17f7835ba27447eb&amp;view=fimg&amp;fur=ip&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ94afFSxbuRshaAeP0IzP42vFfSR41w_CFU97bEgFnSm1Blqng-A8J0ehzKbmdOGaCvXzvIa9Kpdt2TKsk9WwxQuPTPAzx9V47zG2kXcuNwXlUvpYB3YSlTHuY&amp;disp=emb&amp;realattid=ii_l0m6kaj01" alt="Logo" width="120" height="100" data-image-whitelisted="" /></td>
                                             </tr>
                                          </tbody>
                                       </table>
                                    </div>
                                 </td>
                              </tr>
                           </tbody>
                        </table>
                     </td>
                  </tr>
               </tbody>
            </table>
            <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
               <tbody>
                  <tr>
                     <td>
                        <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0" align="center" bgcolor="white">
                           <tbody>
                              <tr>
                                 <td align="center">
                                    <table style="width: 90%;" border="0" cellspacing="0" cellpadding="0" align="center">
                                       <tbody>
                                          <tr>
                                             <td align="center">
                                                <div>
                                                   <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
                                                      <tbody>
                                                         <tr>
                                                            <td valign="middle">
                                                               <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
                                                                  <tbody>
                                                                     <tr>
                                                                        <td align="center">
                                                                           <div><strong>A chance to be in the NFL without getting drafted!</strong>&nbsp;</div>
                                                                        </td>
                                                                     </tr>
                                                                  </tbody>
                                                               </table>
                                                            </td>
                                                         </tr>
                                                      </tbody>
                                                   </table>
                                                </div>
                                             </td>
                                          </tr>
                                       </tbody>
                                    </table>
                                    <table style="width: 90%;" border="0" cellspacing="0" cellpadding="0" align="center">
                                       <tbody>
                                          <tr>
                                             <td align="center">
                                                <div>
                                                   <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
                                                      <tbody>
                                                         <tr>
                                                            <td valign="middle">
                                                               <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
                                                                  <tbody>
                                                                     <tr>
                                                                        <td align="center">
                                                                           <div>Sign up for a career in the league's front office.</div>
                                                                        </td>
                                                                     </tr>
                                                                  </tbody>
                                                               </table>
                                                            </td>
                                                         </tr>
                                                      </tbody>
                                                   </table>
                                                </div>
                                             </td>
                                          </tr>
                                       </tbody>
                                    </table>
                                    <table style="width: 90%;" border="0" cellspacing="0" cellpadding="0" align="center">
                                       <tbody>
                                          <tr>
                                             <td align="center">
                                                <div>
                                                   <table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
                                                      <tbody>
                                                         <tr>
                                                            <td align="center">
                                                               <table border="0" cellspacing="0" cellpadding="0">
                                                                  <tbody>
                                                                     <tr>
                                                                        <td align="center" valign="middle" bgcolor="#ff0000"><a href="https://mail.google.com/mail/u/0/#m_6143428565313462349_link"><span>Sign Up</span></a></td>
                                                                     </tr>
                                                                  </tbody>
                                                               </table>
                                                            </td>
                                                         </tr>
                                                      </tbody>
                                                   </table>
                                                </div>
                                             </td>
                                          </tr>
                                       </tbody>
                                    </table>
                                 </td>
                              </tr>
                           </tbody>
                        </table>
                     </td>
                  </tr>
               </tbody>
            </table>
         </td>
      </tr>
   </tbody>
</table>
    """.format(image_cid=image_cid[1:-1]), subtype='html')

    with open('/Users/rasonirvin/Desktop/onboarding_service/logo.png', 'rb') as img:
       maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
       msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)

    # Log in to server using secure context and send email
    #context = ssl.create_default_context()
    #Create SMTP session for sending the mail
    server = smtplib.SMTP('smtp.gmail.com', 587, timeout=120) #use gmail with port
    server.starttls() #enable security
    server.login(sender, password)
    server.sendmail(sender, recipient, msg)
    server.quit()
    print("Sent Mail to ", recipient[0])