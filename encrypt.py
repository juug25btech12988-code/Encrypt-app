try:
    import pyi_splash # type: ignore
except:
    pass    
#GUI for encrypt2.py
import time
import sys
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog
##Encryption Keys##
alpha_l = {'a':111,'b':124,'c':112,'d':125,'e':113,'f':126,'g':114,'h':127,'i':115,'j':128,'k':116,'l':129,'m':117,'n':130,'o':118,'p':131,'q':119,'r':132,'s':120,'t':133,'u':121,'v':134,'w':122,'x':135,'y':123,'z':136}
alpha_u = {'A':141,'B':154,'C':142,'D':155,'E':143,'F':156,'G':144,'H':157,'I':145,'J':158,'K':146,'L':159,'M':147,'N':160,'O':148,'P':161,'Q':149,'R':162,'S':150,'T':163,'U':151,'V':164,'W':152,'X':165,'Y':153,'Z':166}
num = {'1':191,'2':196,'3':192,'4':197,'5':193,'6':198,'7':194,'8':199,'9':195,'0':200}
misc = {'!':')',')':'!','@':'(','(':'@','#':'*','*':'#','$':'&','&':'$','%':'^','^':'%','-':'+','+':'-','_':'=','=':'_','<':'>','>':'<',',':'.','.':',','/':'?','?':'/',':':':',';':';',"'":'"','"':"'",'{':']',']':'{','}':'[','[':'}',"\\" : "|","|":"\\"}
##/Encryption Keys##

if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, 'encrypti.ico')
else:
    icon_path = 'encrypti.ico'


##functions##
def multiline(mode,title,btntext,root):
    multi_ln = tk.Toplevel(root)
    
    multi_ln.configure(bg='#FFFFFF')
    multi_ln.title(title)
    multi_ln.geometry(f'850x550+{int(sc_width/5)}+{int(sc_height/8)}')
    def get_content(mode):
        content = txt.get('1.0','end')
        if mode == 'en':        #if input is plain text 'to be encrypted'
            global txt_to_encrypt
            txt_to_encrypt = content
            global process_mode
            process_mode = 'en_txt'
        elif mode == 'de':      #if input is encrypted text 'to be decrypted'
            global txt_to_decrypt
            txt_to_decrypt = content
            
            process_mode = 'de_txt'


    multi_ln.rowconfigure(1,weight=1)    
    multi_ln.columnconfigure(2,weight = 1)
    txt = tk.Text(multi_ln, width=85, height=30,bd=0,background='#1A1D23',foreground='#FFFFFF',insertbackground='white',font='Times_New_Roman')
    txt.grid(column=2,row=1,sticky='new',padx=30,pady=5)
    btn = ttk.Button(multi_ln,text=btntext,width=20,command=lambda:[get_content(mode),root.destroy()])
    btn.grid(row=3,column=2,pady=11,ipady=9)

def get_key():
    def retrieve(ent,gkey):
        try:
            tmp = ent.get()
            tmp = float(tmp)
        except ValueError:
            messagebox.showwarning("Error","Incorrect Format")
        else:
            global key 
            key = tmp
            gkey.destroy()   



    gkey = tk.Tk()
    gkey.iconbitmap(icon_path)
    gkey.resizable(False,False)
    gkey.title("Enter Decryption Key")
    gkey.geometry(f'350x150+{spl_x}+{spl_y}')
    lbl = ttk.Label(text="Enter Decryption Key")
    ent = ttk.Entry(textvariable="Enter :",width=40)
    btn = ttk.Button(text='OK',width=15,command=lambda:[retrieve(ent,gkey)])
    for i in range(3):
        gkey.columnconfigure(i,weight=1)
        gkey.rowconfigure(i,weight=1)
    lbl.grid(row= 0, column=1)    
    ent.grid(row=1,column=1)
    btn.grid(row=2,column=1)

    gkey.mainloop()


    

def en_fileopen():
    try:
        filename = filedialog.askopenfile(title="Choose file to encrypt", filetypes=[('text','*.txt')])
        global path
        path = filename.name
        #print(path)
    except AttributeError:
        pass
    except:
        messagebox.showerror("Error","An Unknown Error Has Occured")
    else:
        global process_mode
        process_mode = 'en_file'    #to be encrypted
        

def de_fileopen():
    try:
        filename = filedialog.askopenfile(title="Choose an encrypted file", filetypes=[('text','*.txt')])
        global path
        path = filename.name
        #print(path)
    except AttributeError:
        pass
    except:
        messagebox.showerror("Error","An Unknown Error Has Occured.File could not be opened")    
    else:
        global process_mode
        process_mode = 'de_file'  #to be decrypted 
    

def spl_encrypt():
    splash_encrypt_win = tk.Tk()
    splash_encrypt_win.iconbitmap(icon_path)
    splash_encrypt_win.title("Encrypt")
    splash_encrypt_win.geometry("450x200+{}+{}".format(spl_x,spl_y))
    for i in range(10): #column configure
        splash_encrypt_win.columnconfigure(i,weight=1)
    for i in range(4): #row configure
        splash_encrypt_win.rowconfigure(i,weight=1)
    lbl = tk.Label(splash_encrypt_win, text="Choose An Option")
    txt_btn = ttk.Button(splash_encrypt_win,text="Enter Text", width=20,command=lambda:[multiline('en','Enter text to be encrypted','Encrypt',splash_encrypt_win)])
    file_btn = ttk.Button(splash_encrypt_win,text="Open File",width=20,command=lambda:[en_fileopen(),splash_encrypt_win.destroy() if 'path' in globals() else None])
    lbl.grid(columnspan=10,row=0)
    txt_btn.grid(row=1, column=2, ipady=20)
    file_btn.grid(row=1, column=7, ipady=20)




    splash_encrypt_win.mainloop()


def spl_decrypt():
    splash_decrypt_win = tk.Tk()
    splash_decrypt_win.iconbitmap(icon_path)
    splash_decrypt_win.title("Decrypt")
    splash_decrypt_win.geometry("450x200+{}+{}".format(spl_x,spl_y))
    for i in range(10): #column configure
        splash_decrypt_win.columnconfigure(i,weight=1)
    for i in range(4): #row configure
        splash_decrypt_win.rowconfigure(i,weight=1)
    lbl = tk.Label(splash_decrypt_win, text="Choose An Option")
    txt_btn = ttk.Button(splash_decrypt_win,text="Enter Text", width=20,command=lambda:[multiline('de','Enter encrypted text','Decrypt',splash_decrypt_win)])
    file_btn = ttk.Button(splash_decrypt_win,text="Open File",width=20,command=lambda:[de_fileopen(),splash_decrypt_win.destroy() if 'path' in globals() else None])
    lbl.grid(columnspan=10,row=0)
    txt_btn.grid(row=1, column=2, ipady=20)
    file_btn.grid(row=1, column=7, ipady=20)




    splash_decrypt_win.mainloop()




splash = tk.Tk()
splash.iconbitmap(icon_path)
splash.resizable(False,False)
sc_height = splash.winfo_screenheight()
sc_width = splash.winfo_screenwidth()
#print(sc_width,sc_height)
spl_x,spl_y = int(sc_width/3),int(sc_height/4)
splash.geometry("450x200+{}+{}".format(spl_x,spl_y))
for i in range(10): #column configure
    splash.columnconfigure(i,weight=1)
for i in range(4): #row configure
    splash.rowconfigure(i,weight=1)
    




splash.title("Encrypt/Decrypt")
spl_header_lbl = tk.Label(splash,text="Choose An Option")
spl_header_lbl.grid(columnspan=10,row=0)
spl_encrypt_btn = ttk.Button(splash, text="Encrypt", width=20,command=lambda:[splash.destroy(),spl_encrypt()])
spl_encrypt_btn.grid(row=1, column=2, ipady=20)
spl_decrypt_btn = ttk.Button(splash, text="Decrypt", width=20,command=lambda:[splash.destroy(),spl_decrypt()])
spl_decrypt_btn.grid(row=1, column=7, ipady=20)
try:
    pyi_splash.close()
except:
    pass    
splash.mainloop()
#                 #
##processing text##
#                 #
#print(process_mode)
try:
    if process_mode == 'de_file' or process_mode == 'de_txt':
        get_key()
except:
    pass        
    #print(key)
###core function import pending

def encrypt(txt_to_encrypt):
    etime = time.time()
    usr_inp = txt_to_encrypt
    mod_list = []
    for char in usr_inp:
        mod_list.append(char)
        mod_list.append('~`')
    #print(mod_list)
    ####

    final_str = ''
    for i in mod_list:
        if i == ' ':
            final_str += ' '
        elif i == '\n'    :
            final_str+= '\n'
        elif i in alpha_l:
            val = alpha_l.get(i)
            temp = val*etime
            final_str += str(temp)
        elif i in alpha_u:
            val = alpha_u.get(i)    
            temp = val*etime
            final_str += str(temp)
        elif i in num:
            val = num.get(i)    
            temp = val*etime
            final_str += str(temp)
        elif i == '~`':
            final_str += '~`'
        elif i in misc:
            temp = misc.get(i)    
            final_str += temp
        #elif i == '\n':
            #print('\n')
        else:
            final_str += i
    global encryp_code        
    encryp_code =final_str.rstrip('~`')
    #print("Your text has been sucessfully encrypted")        
    #print("Kindly note down the following key to decrypt:\n",etime)
    #print(''*3)
    #print("Encrypted Code:")
    #print(final_str.rstrip('~`'))
    #print(''*2)

    encrypt_win = tk.Tk()
    encrypt_win.iconbitmap(icon_path)
    encrypt_win.title("Encrypted Text")
    encrypt_win.geometry(f'850x550+{int(sc_width/5)}+{int(sc_height/8)}')
    encrypt_win.rowconfigure(1,weight=1)    
    encrypt_win.columnconfigure(2,weight = 1)
    txt = tk.Text(encrypt_win, width=85, height=30,bd=0,background='#1A1D23',foreground='#FFFFFF',insertbackground='white',font='Times_New_Roman')
    txt.grid(column=2,row=1,sticky='new',padx=30,pady=5)
    txt.insert('1.0','Your text has been successfully encrypted.\n')
    txt.insert('2.0','Kindly note down the following key to decrypt:\n')
    txt.insert('3.0',etime)
    txt.insert('4.0','\n\nEncrypted Code:\n\n')
    txt.insert('8.0',encryp_code)
    btn = ttk.Button(encrypt_win,text='Close',width=20,command=lambda:[encrypt_win.destroy()])
    btn.grid(row=3,column=2,pady=11,ipady=9)
    encrypt_win.mainloop()


##decryption
def decrypt(txt_to_decrypt,key):
    enc_str = txt_to_decrypt.rstrip('\n')
    ekey = key
    en_l = enc_str.split('~`')
    #print(en_l)
    dec_list =[]
    for i in en_l:
        try:
            i = float(i)
        except:
            pass    
        if type(i) == float:
            dec_key = float(i)/ekey
            dec_key = round(dec_key)
            #print(dec_key)
            #print('')
            dec_list.append(int(dec_key))
        else:
            dec_list.append(i)

    #print(dec_list)        
    decrypt_l =[]

    #finding key from value
    try:
        for code in dec_list:
            if str(code) == ' 'or str(code) == '':
                decrypt_l.append(str(code))
            elif str(code) == '\n'    :
                decrypt_l.append('\n')
            elif code in misc:
                for key in misc:
                    if misc[key] == code:
                        decrypt_l.append(key)
                        break   
            elif int(code) > 110 and int(code) < 137: #alpha_l
                for key in alpha_l:
                    if alpha_l[key] == code:
                        decrypt_l.append(key)
                        break
            elif int(code) >140 and int(code) < 167: #alpha_u
                for key in alpha_u:
                    if alpha_u[key] == code:
                        decrypt_l.append(key)
                        break
            elif int(code) > 190 and int(code) < 201: #num
                for key in num:
                    if num[key] == code:
                        decrypt_l.append(key)
    except Exception as e:
        #print(e)
        #print("An Error occured while Decrypting. Re-check Encrypted code or key.")
        messagebox.showerror("Error","An Error occured while decrypting.")                    
        spl_decrypt()
    #print(decrypt_l)
    decrypt_str = ''
    for i in decrypt_l:
        decrypt_str += i
    #print("Decrypted string:",decrypt_str)

    decrypt_win = tk.Tk()
    decrypt_win.iconbitmap(icon_path)
    decrypt_win.title("Decrypted Text")
    decrypt_win.geometry(f'850x550+{int(sc_width/5)}+{int(sc_height/8)}')
    decrypt_win.rowconfigure(1,weight=1)    
    decrypt_win.columnconfigure(2,weight = 1)
    txt = tk.Text(decrypt_win, width=85, height=30,bd=0,background='#1A1D23',foreground='#FFFFFF',insertbackground='white',font='Times_New_Roman')
    txt.grid(column=2,row=1,sticky='new',padx=30,pady=5)
    txt.insert('1.0',decrypt_str)
    btn = ttk.Button(decrypt_win,text='Close',width=20,command=lambda:[decrypt_win.destroy()])
    btn.grid(row=3,column=2,pady=11,ipady=9)
    decrypt_win.mainloop()





#calling function
try:
    if process_mode == 'en_txt':
        encrypt(txt_to_encrypt)
    elif process_mode == 'de_txt':
        decrypt(txt_to_decrypt,key)
    elif process_mode == 'en_file'    :
        with open(path) as f:
            data = f.read()
            encrypt(data)
    elif process_mode == 'de_file'        :
        with open(path) as f:
            data = f.read()
            decrypt(data,key)
except:
    pass           