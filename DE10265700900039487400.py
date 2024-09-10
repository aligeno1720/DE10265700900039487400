import socket
import subprocess
import os
import sys
import time
def connect_to_server(server_ip, server_port):
    try:
        # Create a socket object using the socket.AF_INET and socket.SOCK_STREAM (TCP)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server (IP address and port)
        client_socket.connect((server_ip, server_port))
        print(f"Connected to server {server_ip} on port {server_port}")
        
        # Send data to the server
        message = "WELCOME SERVER TO SERVER ...!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent message: {message}")
        
        # Receive data from the server
        response = client_socket.recv(0000)  # Receive up to 1024 bytes
        print(f"Received from server Target: {response.decode('utf-8')}")
        
    except socket.error as e:
        print(f"Error connecting to server: {e}")
    finally:
        # Close the connection
        client_socket.close()
        print("Connecting...")

def run_wget():
    # Get the website URL from the user
    url = input("Enter the website URL Target: ")
    
    # Construct the wget command for mirroring the website
    wget_command = ["wget", "--mirror", url]
    
    # Run the wget command
    try:
        result = subprocess.run(wget_command, check=True)
        print("Website mirrored successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running wget: {e}")

# Get the server IP and port number from the user
server_ip = input("Enter server IP address: ")
server_port = int(input("Enter server port number: "))

# Connect to the server using the user-provided IP and port
connect_to_server(server_ip, server_port)

# Run wget to mirror a website after the connection is established
run_wget()
#===================================================================================
# Define the text content
text = "---------Welcome to Cloud Cyber Security GlobalServer Software ©2024-All Rights Reserved.-----------"

# Define the background color code (ANSI escape code) background_color_code = "\033[48;5;226m"
#background_color_code = "\033[47;5;226m" backgroundnya putih
#background_color_code = "\033[46;5;226m" backgroundnya hijau
#background_color_code = "\033[30;5;226m" backgroundnya kosong tapi tulisannya putih
background_color_code = "\033[48;5;226m"

# Define the reset code (to reset the formatting)
reset_code = "\033[0m"

# Create the block-colored text
block_colored_text = f"{background_color_code}{text}{reset_code}"
print("="*100)

# Print the block-colored text
print(block_colored_text)
print("="*100)


username = input("Enter Username : ")
if username == "********************" :
    time.sleep(2)
username = input("Enter Password : ")


def dot_loading(duration, interval=0.5, max_dots=10):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(max_dots + 1):
            sys.stdout.write('\rLoading' + '.' * i + ' ' * (max_dots - i))
            sys.stdout.flush()
            time.sleep(interval)
    sys.stdout.write('\rLoading' + '.' * max_dots + '\n')  # Ensure the last line is complete
    sys.stdout.flush()

if __name__ == "__main__":
    duration = 5  # Duration in seconds
    dot_loading(duration)
    print("ACCESS GRANTED!")    
    time.sleep(2)
    # Define the text content
    text = "-------------------------------------------WELCOME ADMIN--------------------------------------------"
   
# Define the background color code (ANSI escape code)
    background_color_code = "\033[48;5;226m"

# Define the reset code (to reset the formatting)
    reset_code = "\033[0m"

# Create the block-colored text
    block_colored_text = f"{background_color_code}{text}{reset_code}"
    print("="*100)

# Print the block-colored text
    print(block_colored_text)
    print("="*100)

from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time
current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the current date and time with seconds
print("https://www.ipdb.com ====>>>Servertoserver-193.150.166.18/193.150.166.152-",current_date_time )
time.sleep(1)
print("https://www.ipdb.com/DEUT-HEBA42893090/raw-data/fileAsset?language_id=Rr1name/e-banking2db,com>>>messagetransmitted<<<")
time.sleep(2)

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
   
    # Create a color sequence
    color_seq = [
        '\033[91m',  # Red
        '\033[93m',  # Yellow
        '\033[92m',  # Green
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[96m'   # Cyan
    ]
   
    bar = ''
    for i in range(length):
        if i < filled_length:
            bar += color_seq[i % len(color_seq)] + fill + '\033[0m'
        else:
            bar += ' '

    # Print the progress bar
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

# Example usage
if __name__ == "__main__":
    total = 100
    for i in range(total + 1):
        print_progress_bar(i, total, prefix='Progress:', suffix='Complete', length=88)
        time.sleep(0.05)
    print()  # Move to the next line after the progress bar completes


# Get the current date and time
now = datetime.now()

# Format the date and time
current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the current date and time with seconds
print("CONNECTED!",current_date_time )
time.sleep(1)
# Define color codes (ANSI escape codes)

RED = "31"
GREEN = "32"
BLUE = "34"
WHITE = "37"

# Example usage
sentence = f">>>>>>>>>>>>>>>  {color_text('successfully built>>>>SRV1>>>NAME-EBANKINGCH2:DB.COM', WHITE)}"
print(sentence)
sentence = f">>>>>>>>>>>>>>>  {color_text('successfully built>>>>SRV2>>>NAME-EBANKINGCH2:DB.COM', WHITE)}"
print(sentence)
sentence = f">>>>>>>>>>>>>>>  {color_text('successfully built>>>>SRV3>>>NAME-EBANKINGCH2:DB.COM', WHITE)}"
print(sentence)
time.sleep(5)
sentence = f">>>>>>>>>>>>>>>  {color_text('ns1.db.com.de(23.62.20.68)ns21.db.net(204.13.250.141)ns20.db.net(208.78.70.141)ns11.db.com.de)', WHITE)}"
print(sentence)
time.sleep(1)
sentence = f">>>>>>>>>>>>>>>  {color_text('(23.62.20.68)193.112.80.1 193.112.80.2 193.112.80.3 193.112.80.4 193.112.80.5 193.112.80.10', WHITE)}"
print(sentence)
time.sleep(1)
sentence = f">>>>>>>>>>>>>>>  {color_text('23.62.20.681 193.112.80.12 193.112.80.13 193.112.80.14 193.112.80.15 193.112.80.16', WHITE)}"
print(sentence)
time.sleep(1)
sentence = f">>>>>>>>>>>>>>>  {color_text('23.62.20.68 193.112.80.19 193.112.80.20 193.112.80.21 193.112.80.22 193.112.80.23 ', WHITE)}" 
print(sentence)
time.sleep(1)
sentence = f">>>>>>>>>>>>>>>  {color_text('23.62.20.68 193.112.80.25 193.112.80.26 193.112.80.27 193.112.80.28 193.112.80.29 ', WHITE)}"
print(sentence)
time.sleep(1)
sentence = f">>>>>>>>>>>>>>>  {color_text('23.62.20.68 193.112.80.31 193.112.80.32 ', WHITE)}"
print(sentence)
time.sleep(1)

from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time
current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
time.sleep(5)
#==================================================================
# ANSI escape codes for text formatting
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Function to get the current date and time in the desired format
def get_current_datetime():
    return datetime.now().strftime("%d.%m.%Y / %H:%M:%S")

# Typewriter effect function
def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Function to apply color formatting
def colorize_text(text):
    """Colorizes text before and after the colon."""
    if ':' in text:
        # Split text into before and after the colon
        before_colon, after_colon = text.split(':', 1)
        # Apply green color to the text before the colon and red to the text after
        return f"{GREEN}{before_colon} :{RESET}{RED}{after_colon}{RESET}"
    else:
        return f"{GREEN}{text}{RESET}"

# Function to display the message with updated date and time
def display_server_message():
    # Message header
    server_to_server = "SERVER TO SERVER        : DELIVERY"
    from_info = "FROM                    : DEUTDE3B265"
    subject = "SUBJECT                 : VIA SERVER TO SERVER"
    date_time = f"DATE/TIME               : {get_current_datetime()}"
     # Additional details
    report_time_zone = "Report time zone        : +002GMT"
    delivery_date_time = f"Delivery date & time    : {get_current_datetime()}"
    transaction_code = "Message Transaction Code: DEUTDE3BXXX/DEUTDEFFXXX"
    # Final message section
    messages = (
        "Your messages are shown below:",
        "From: DEUTSCHE BANK AG",
        "CET-PG 01 service message number: DEUT889264020586",
        "(CET) Ordering Customer: A&E VERWALTUNGS GMBH & CO"
    )
    time.sleep(9)
    # Typewriter style display of the message
    typewriter(colorize_text(server_to_server))
    typewriter(colorize_text(from_info))
    typewriter(colorize_text(subject))
    typewriter(colorize_text(date_time))
    typewriter("")  # Empty line for spacing
    typewriter(colorize_text(report_time_zone))
    typewriter(colorize_text(delivery_date_time))
    typewriter(colorize_text(transaction_code))
    typewriter("")  # Empty line for spacing
    
    # Display additional message details
    for message in messages:
        typewriter(message)

# Call the function to display the message
display_server_message()

#================================================================================================================================
import sys
import time

def progress_bar(iteration, total, prefix='', suffix='', length=80, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

# Example usage
total_iterations = 100

for i in range(total_iterations + 1):
    time.sleep(0.05)  # Simulate some work
    progress_bar(i, total_iterations, prefix='Progress:', suffix='', length=75)#setelah suffix bisa ditambahin kata2

print("\ncompleted!")

import date
from datetime import datetime

def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"Current Date and Time: {current_time}")

#time.sleep (10)
#================================================================================================================================
import time
import sys
from datetime import datetime

# ANSI escape codes for red color
RED = '\033[91m'
RESET = '\033[0m'
# Define constants for text formatting
RED = '\033[91m'   # Red text
WHITE = '\033[97m' # White text
RESET = '\033[0m'  # Reset formatting
# Function to simulate typewriter effect
def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Function to apply red color after ":"
def colorize_after_colon(text):
    if ':' in text:
        before_colon, after_colon = text.split(':', 1)
        return f"{before_colon}:{RED}{after_colon}{RESET}"
    return text

# Get the current date and time
now = datetime.now()

# Format the date and time
current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the current date and time with seconds
print("CONNECTED!",current_date_time )
time.sleep(1)
# Function to display the S2S message
def display_s2s_message():
    # Red header
    header = f"{WHITE}---------------------------------S2S SPECIAL TRANSFER SWIFT MESSAGE TRANSMISSION-----------------------------------------------{RESET}"
    
    # Message details
    message_lines = [
        "DEUT//: 004: /Bank Sender Account Number            : DE10265700900039487400",
        "DEUT//: 006: /Bank Sender Swift                     : DEUTDE3B265",
        "DEUT//: 008: /Bank Sender Global IP                 : 193.150.166.18/193.150.166.152",
        "DEUT//: 010: /Bank Sender Network Delivery Status   : Global ACK",
        "DEUT//: 012: /Bank Sender IMAD Number               : 0000SRT-RN-440-553822BEH22RLNO0O",
        "DEUT//: 014: /Bank Global Server ID                 : AS8373",
        "DEUT//: 016: /Bank WTS Server                       : s020005635",
        "DEUT//IP//DB: SERVER...",
        "l://ipdb.com 0://ip 0 name-ip banking 0",
        "2://ipdb.com 1://ip name-ip banking 1",
        "3://ipdb.com 2://ip name=ip banking 2",
        "DEUT//: 022: /DB Identity Code                      : DE78348DB382XX",
        f"DEUT//: 024: /Bank Input Global Time                : {datetime.now().strftime('%d %B, %Y %H:%M:%S')}",
        "DEUT//: 026: /Client Sender Account Holder          : AsE VERWALTUNGS GMBH & CC",
        "DEUT//: 028: /IP/IP Code                            : DE36728910255DB",
        "DEUT//: 032: /Clearing Code                         : DEUT-HEBA42893090",
        "DEUT//: 034: /Client Bank                           : DEUTSCHE BANK AG",
        "DEUT//: 036: /Client Bank Address                   : WITTEKINDSTRASSE 9-10, 49074 OSNABRUECK, GERMANY",
        "DEUT//: 038: /Client Swift Code                     : DEUTDE3B265",
        "DEUT//: 040: /Common Account Number                 : 947256564"
    ]
    
    # Display red header
    typewriter(header)
    
    # Display message lines with typewriter effect, coloring after ':'
    for line in message_lines:
        typewriter(colorize_after_colon(line))

# Call the function to display the S2S message
display_s2s_message()
time.sleep(5)
#================================================================================================================================
import time
import sys
from datetime import datetime

# ANSI escape codes for text formatting
HEADER = '\033[94m'  # Blue color for header
CERTIFICATE = '\033[91m'  # Red color for certificate
INFO = '\033[92m'    # Green color for information text
RESET = '\033[0m'    # Reset color

# Function to simulate typewriter effect
def typewriter(text, delay=0.03): #=============================================changed
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
#======================================================================== certificate
from datetime import datetime

# Define constants for text formatting
HEADER = "\033[1;34m"  # Blue text
CERTIFICATE = "\033[1;32m"  # Green text
RESET = "\033[0m"  # Reset formatting

def display_message():
    """
    Display a formatted message including ending time, certificate, and transmission details.
    """
    # Get the current time and format it
    ending_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Define the certificate and transmission details
    certificate_content = (
        "zVi$Nz6hTLrs5QoJtlCZYq*SVo%9Oi4W*{?fzKjYiNl@RtZAMBib1z${$8Af~uRABw}2PzOAPOtu5dADEP@KNou{2muyPt?lc0TpJ0Z?r#9 "
        "P{H8X9?XkGnMIA?*#R}fUvp%4@I5S7O{Ibbkb}RWhh5pj?WsGVhi}82B|QiSvB|AOtu|8H#nxk91H}5|Yd|HXpnH4eC1zqn2fYlK5uDBey5 "
        "9i30V0iJ9NL@j2~GXHpHXtoO{56q7Kc$*{TuoEUPUluAzbXS#53oopxpN{EzBlZFLJdLzoPO~JxCtM3u4TjAPWrFb8kojJNj@71A4gZDEr2 "
        "slTA3D1d1xP$84G3le%|D|738p5pMiWpEj@m~5x1RgXx5tU?UC7ug03HFWTT7k{JJkYV~ehmKlA3yrd~?lNIx*fDR}M8Ju6Ysl#M02HW%VP "
        "HC4J22B##2ClmE?deeIhvA4g0}b~3k$RC$n8@}MxSOPpahyZYKFIJ6lGZq|R4XsgRXNfa}tYMOSf3BFoVHWdVH4R2~mm494FO22p|F68?g8 "
        "T$8e6iVyJ3j}kTtLzelqlWnlah8~%@HkwexxPoy~*{z8h}CtKYc4f4?B5ApJ@LZ~4$I*UqqBKW|ZJvOJ2R@a*cCWNc$sJj8wwgtdhKTTAK% "
        "q|R~F~8Dx7bvXkCYMg3HhEZRVq*}}kUXjtzs2vkXBaa?6qfHR2CA5qgsNJVHoE{wrezf?iKs}kVpCwh6~pzdQSztpC~P5G4Jfb|5yFB6pa{ "
        "ii4}ruC5V~a@wuZQ#1mBo7mgRLkn%amrQJ*3GpMy8Xvsmi|7*N8YpsM#r?apg@ya#2WDP8Gkoh$MNfutS$loK$Nl4uP5Ms$7#IAetNc0% "
        "?tikYInD37$4J6j?e4nLv|TQq0EiG@%@XF~zSyEa6YuH5kitnAShhCajDZ3T8A{J8ftU1cdVk64dpNKu6uhJhnT@fOdC4mEi0uQ5|nL6vfp "
        "72*I|t#@MINjk46#nBijuKQxscZL}2CyYfao~#0%V9eyRml@nJvbeP99zEhZV%Fi1q~paqZJRooMrb1K#~U*G5#pB%Dumg?#BamntOJ|Sx0 "
        "t$y~?o0PTL?TLQ2beZCzF#*MBY%7jBa@{d~FYSV*ZZxRNNJc}M9bhia6doIRx86H~jC{MYuwb03Hx#1~#11}TCIQ~M|e~3x3R017sb|3w*6 "
        "63iJNxkIY@lFeQ5ox?IIX#Nx#4tHSOJnkXSA6Pwgi%SPKFIQXm2MYXiMo7wH@8y01pb{QGUdzdZthf|4*WwGp95@6wcvV*BJBLyb5u%E15} "
        "BjoYQuQ{gXYpig9w3$V2ey~r*BtgqhhckPZtQCIQs0?#cMpL?{6e4a1#{%vR1N3W%R#ux?LHoQ~4~mRhx9}aoa53@2KIdxt4CKIpGe$O6~d "
        "n~qJeiTj5hAGDo@uYZQwCacIKFICxT9#yzZr${09E63~m@uE6L0f2~dYxiH9}ZgyZKnDG{M$XMWJkStA4nSkQg*%I25QWI7GBzfw9TQtA "
        "m}0Lw$2LxEBW$7t{M?G0u#~EBrWNX03tL{cOqEMEsh~qHAMlSK@C6*#FQvMnjEQQC#P6GoSOByWNkbeSu1Suo@3EG~oSRiBS#0q8uYf6iif "
        "XszN4{uw6BE$Dpq4M2gN$ZPEHVwR9DX?FT0TE01wuHR?9B7|VNrBFzVl~yJMeyG?XpjT1Wy8SjWnftOpT1xjN0X$cKt#q}RX1B~Ib9H||no "
        "zP~6U$@of1ql6*T$9Zw?mMGa0nb58dR%MJUrKMWS2j3kJ47LgaJIvXt|r3RjOPY3}OHvjOq}o@ubq|8*egqNY%yEciaSZ0H8Gpg03~CkeYg "
        "s6nGJJbC|?2AjdUp$St#LvqwXEDa|9Mj|Cpfw@?YF}7wlOqN5{raU{fTf@nOIhl%fcF~Qxf~D{C5fEthD"
    )
    time.sleep (5)
    
    transmission_details = (
        "SENDER AMOUNT                                                    : 50, 000,000,000.00#EUR# \n"
        "TRANSMITTING BANK                                                : DEUTSCHE BANK AG \n"
        "BANK ADDRESS                                                     : WITTEKINDSTRASSE 9-10, 49074 OSNABRUECK, GERMANY \n"
        "SWIFT CODE                                                       : DEUTDE3B265 \n"
        "CABLE IP/IP ADDRESS                                              : 28173277361527/2946DB3728 \n"
        "IPSERV//PERMIT ARRIVAL MONEY                                     : SCF-832J573SK482  \n"
        "IPSERV//DEPOSIT CODE                                             : U42936-9173-482 \n"
        "IPSERV//BLOCKING CODE                                            : SET BY RECEIVING BANK \n"
        "IPSERV//UTR CODE                                                 : DEUT927089014783 \n"
        "IPSERV//REFERENCE CODE                                           : 2731-4173-U4728-IS645-DEUTXX4729883472934618 \n"
        "IPSERV//FED CODE                                                 : FED|372891725.362716253.718233.471825 (NOT COPY) \n"
        "IPSERV//SECURITY CODE                                            : SET BY RECEIVING BANK \n"
        "IPSERV//WITHDRAWAL FED CODE                                      : SET BY RECEIVING BANK \n"
        "IPSERV//INTERNATIONAL DEPOSIT CODE                               : DB37293866DTL2L/NO.46782-CA-46781 \n"
        "IPSERV//MILLION/BILLION DEPARTMENT FRANKFURT                     : ART/Y- LAW-21-FRANKFURT GOVERNMENT, TCL 75342 \n"
        "IPSERV//ONE TIME SATELLITE SWIFT DOWNLOAD ACCESS WITHDRAWAL CODE : 6782836478.0JS46274H52.DB372"
    )

    # Format the message details
    header = f"{HEADER}ENDING TIME : {ending_time}{RESET}"
    certificate_header = f"{CERTIFICATE}-----------------------------------------------------BEGIN CERTIFICATE------------------------------------------------------------{RESET}"
    certificate_footer = f"{CERTIFICATE}------------------------------------------------------END CERTIFICATE-------------------------------------------------------------{RESET}"
    transmission_header = f"{HEADER}--------------------------------------------------SENDER S2S TRANSMISSION------------------------------------------------------------{RESET}"

    # Print the formatted messages
    print(header)
    print(certificate_header)
    print(certificate_content)
    print(certificate_footer)
    print(transmission_header)
    print(transmission_details)

def main():
    """
    Main function to run the script tasks.
    """
    # Call the function to display the message
    display_message()

    # Additional script logic can be added here
    print("Additional script tasks can be executed here.")

if __name__ == "__main__":
    main()
#======================================================================== certificate

# Function to display the message with typewriter effect

def dot_loading(duration, interval=0.1, max_dots=10):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(max_dots + 1):
            sys.stdout.write('\rLoading' + '.' * i + ' ' * (max_dots - i))
            sys.stdout.flush()
            time.sleep(interval)
    sys.stdout.write('\rLoading' + '.' * max_dots + '\n')  # Ensure the last line is complete
    sys.stdout.flush()
time.sleep (8)
import time
import sys

# ANSI escape codes for box formatting
HEADER = '\033[94m'  # Blue color for the header
BOX_LINE = '\033[95m'  # Purple for the box lines
RESET = '\033[0m'  # Reset color

# Function to simulate typewriter effect
def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
#=======================================================================================
import sys
import time

# ANSI escape codes for text formatting
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Function to simulate typewriter effect
def typewriter(text, delay=0.03):
    """Simulates a typewriter effect by printing text one character at a time."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Function to colorize entire line in green
def colorize_green(text):
    """Colors entire line in green."""
    return f"{GREEN}{text}{RESET}"

# Function to display table with typewriter effect
def display_table():
    """Displays the table with typewriter effect."""
    table_lines = [
        "+====+====================================+=================================+",
        "| 1. | IDENTITY CODE/FINAL CODE           : DE44018DB074XF                  |",
        "| 2. | INTERBANK BLOCKING CODE            : 32896:S/T0/S:373287             |",
        "| 3. | SORT CODE                          : 20240202S44081S464407200-DE     |",
        "| 4. | RELEASE CODE                       :                                 |",
        "| 5. | ACCESS CODE                        : DEUT-46293402                   |",
        "| 6. | TRANSACTION CODE                   : DEUTDE3BXxX/DEUTDEFEXXX         |",
        "| 7. | SETTLEMENT TRANSACTION CODE        : 7831 9837 J3729482              |",
        "| 8. | FINAL BLOCKING CODE                : DEUT889264020586                |",
        "| 9. | FINAL CODE                         :                                 |",
        "| 10.| TRANSFER CODE                      :                                 |",
        "| 11.| SOURCE TRANSACTION ID              : 144A:S:G4639DVY8                |",
        "| 12.| WTS SERVER                         : L020623DEUTDE3B182637017        |",
        "| 13.| BONDING KEY                        : S020005635                      |",
        "| 14.| USER NAME                          : hDg462Us742 472837H3 5          |",
        "| 15.| UTR CODE                           : DEUT1102657900                  |",
        "| 16.| TERMINAL ID                        : TERMINAL44839457294             |",
        "| 17.| DOWNLOADING CODE                   : JS-4627-K-98726-46781-92380     |",
        "| 18.| RECEIVING CODE                     : 504-3726-8276-384-0982          |",
        "| 19.| ACTIVATION CODE                    : TD-38296-J-38927-362871-83764   |",
        "| 20.| BIS TRANSACTION                    : UFG4473827546293847227483       |",
        "+====+====================================+=================================+"
    ]
    
    # Display the table with typewriter effect and green color
    for line in table_lines:
        typewriter(colorize_green(line))

# Main execution
def main():
    display_table()

if __name__ == "__main__":
    main()
#=============================================================================================
    
import time
import sys
from datetime import datetime

# ANSI escape codes for text formatting
HEADER = '\033[94m'  # Blue color for header
INFO = '\033[92m'    # Green color for information text
RESET = '\033[0m'    # Reset color

# Function to simulate typewriter effect
def typewriter(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Function to display the message with ending time
def display_officer_authorization():
    # Get the current time and format it
    ending_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Header and message details
    header = f"{HEADER}ENDING TIME : {ending_time}{RESET}"
    bank_name = f"{INFO}DEUTSCHE BANK AG{RESET}"
    authorization = f"{INFO}OFFICERS AUTHORIZATION{RESET}"
    
    officers = [
        "Mr. James Von Moltke                      Mr. Olivier Vigneron",
        "Chief Financial Officer                   Chief Risk Officer",
        "PIN: 54082                                68274",
        "SSN: 4400835",
        "ZIP CODE: 0327",
        "SIC CODE: 9231",
        "DIRECTOR ID: 632896099",
        "STEUR ID: DEO0O5140008"
    ]
    
    encrypted_message = "ENCRYPTED CIPHERED ENDTRANSMS: DE47629.518747.9314509026.DEUT.2881169"
    transmitter = "Transmitter v7.9.VURDFV5920P31DEFF-6"
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time
current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
time.sleep(5)
#==================================================================
# ANSI escape codes for text formatting
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Function to get the current date and time in the desired format
def get_current_datetime():
    return datetime.now().strftime("%d.%m.%Y / %H:%M:%S")
    # Displaying the message
    typewriter(header)
    typewriter(bank_name)
    typewriter(authorization)

    for officer in officers:
        typewriter(officer, delay=0.01)

    typewriter(encrypted_message)
    typewriter(transmitter)

# Call the function to display the message
display_officer_authorization()

from datetime import datetime

# Define constants for text formatting
HEADER = "\033[1;34m"  # Blue text
URL_FORMAT = "\033[1;32m"  # Green text
RESET = "\033[0m"  # Reset formatting

def display_message(url):
    """
    Display a formatted message including ending time and user-provided URL.
    """
    # Get the current time and format it
    ending_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted message
    print(f"{HEADER}Operation Ended at {ending_time}{RESET}")
    print(f"{URL_FORMAT}Access the site here: {url}{RESET}")

# Get user input
url = input("Please enter the URL : ")

# Call the function to display the message with the user-provided URL
display_message(url)
time.sleep (10)
