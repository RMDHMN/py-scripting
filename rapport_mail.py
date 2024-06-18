
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from datetime import datetime

# Configuration de l'e-mail
smtp_server = 'smtp.gmail.com'  
smtp_port = 587  
smtp_user = 'pro.instinct.213@gmail.com'  # Votre adresse e-mail
smtp_password = 'hlsf zfag dxbn pyuk'  # Votre mot de passe d'e-mail

from_email = 'pro.instinct.213@gmail.com'
to_email = 'luc.peres@carbon-it.com'  # Adresse e-mail du destinataire

# Génération du rapport quotidien 
def generate_report():
    today = datetime.now().strftime('%Y-%m-%d')

    # Test à faire ici 
    
    ####
    ####
    ####

    report_content = f"Rapport quotidien pour le {today}\n\nTout fonctionne normalement."
    
    report_filename = f"rapport_{today}.txt"
    with open(report_filename, 'w') as file:
        file.write(report_content)
    
    return report_filename

# Fonction pour envoyer l'e-mail avec le rapport en pièce jointe
def send_email_with_report():

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = f"Rapport quotidien - {datetime.now().strftime('%Y-%m-%d')}"
    

    body = "Veuillez trouver ci-joint le rapport quotidien."
    msg.attach(MIMEText(body, 'plain'))
    
    # Génération du rapport et ajout en pièce jointe
    report_file = generate_report()
    with open(report_file, 'rb') as file:   
        part = MIMEApplication(file.read(), Name=os.path.basename(report_file))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(report_file)}"'
        msg.attach(part)
    
    # Envoi de l'e-mail
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("E-mail envoyé avec succès")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail: {e}")
    finally:
        # Suppression du fichier de rapport après envoi
        os.remove(report_file)


if __name__ == "__main__":
    send_email_with_report()

