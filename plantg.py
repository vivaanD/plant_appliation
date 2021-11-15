from tkinter import *
from tkinter import ttk
import webbrowser
root = Tk()
root.geometry("550x150")
root.title('Planticulture')
stage = 1
help_w_val = [
    'maintenance and care',
    'fertilizers',
    'pest control',
    'soil',
    'seeds'
]
state_val = [
    'your state',
    'Andhrapradesh',
    'Arunachal pradesh',
    'Maharashtra',
    'Assam',
    'Bihar',
    'Chattisgarh',
    'Goa',
    'Gujarat',
    'Haryana',
    'Madhyapradesh',
    'Himachalpradesh',
    'Jambu and Kashmir',
    'Jharkhand',
    'Kerala',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil nadu',
    'Telangana',
    'Tripura',
    'Uttar pradesh',
    'Uttarakhand',
    'West bengal',
    'Delhi'
]
lang_val = [
    'your preferred language',
    'tamil',
    'english',
    'hindi',
    'marathi',
    'kannada',
    'telugu',
    'gujarati',
    'bengali'
]
exp_val = [
    'your experience level with plantation',
    'beginner',
    'intermediate',
    'expert'
]
i = ''
si = ''
first = True
experience = ''
count = 1
language = ''
state = ''
# survey


def state_change():
    global exp, state, lang, experience, count, language
    print(count)
    if count == 1:
        welcome_label.destroy()
        welcome_label2.destroy()
        welcome_label3.destroy()
        lang.grid(row=1, column=1)
        exp.grid(row=2, column=1)
        lang_l.grid(row=1, column=2)
        exp_l.grid(row=2, column=2)
        state_a.grid(row=3, column=1)
        state_l.grid(row=3, column=2)
        count += 1
    elif count == 2:
        if str(exp.get().title()) != "" and str(exp.get()) != 'your experience level with plantation':
            if str(lang.get().title()) != "" and str(lang.get()) != 'your preferred language':
                if str(state_a.get().title()) != "" and str(state_a.get()) != 'your state':
                    language = language + str(lang.get())
                    state = state_a.get()
                    experience = exp.get()
                    exp.destroy()
                    lang.delete(0, END)
                    lang_l.config(text="Type the plant which you would want to grow")
                    continue_button.config(text="search", command=search)
                    count += 1
                    exp.destroy()
                    exp_l.config(text="you need help in which area")
                    plant_n.grid(row=1, column=1)
                    help_in_area.grid(row=2, column=1)
                    lang.destroy()
                    state_a.destroy()
            else:
                if count >= 2:
                    lang_l.config(text="this is a required field")
                    count -= 1
        else:
            if count >= 2:
                exp_l.config(text="this is a required field")
                count -= 1


def survey_stage_1():
    global welcome_label
    global welcome_label2
    global welcome_label3
    welcome_label = Label(main_frame, text='welcome to the planticulture, your expert adviser')
    welcome_label2 = Label(main_frame, text='for all types of plantation related queries')
    welcome_label3 = Label(main_frame, text='click on continue to proceed')
    welcome_label.pack()
    welcome_label2.pack()
    welcome_label3.pack()


def change_state():
    global stage
    stage += 1
    print(stage)


def url_generater(ii):
    global first
    global si
    if str(plant_n.get()) != "":
        si = ''
        i2 = ii.split()
        for s in i2:
            if first:
                first = False
                si += s
            elif not first:
                si += f'+{s}'
        url = f"https://www.google.com/search?q={si}"
        print(url)
        return url
    else:
        lang_l.config(text="this is a required field")


def search():
    print(count)
    ii = f'''{help_in_area.get()} for {plant_n.get()} plant cultivation in {state} for {experience} in 
         {language} language'''
    result_url = url_generater(ii)
    webbrowser.open(result_url)


main_frame = Frame(root)
main_frame.grid(row=0, column=1, pady=10, padx=20)
continue_button = Button(root, text="continue", command=state_change)
continue_button.grid(row=1, column=1)
lang = ttk.Combobox(main_frame, value=lang_val)
lang.current(0)
exp = ttk.Combobox(main_frame, value=exp_val)
exp.current(0)
lang_l = Label(main_frame, text="")
exp_l = Label(main_frame, text="")
plant_n = Entry(main_frame)
state_a = ttk.Combobox(main_frame, value=state_val)
state_a.current(0)
state_l = Label(main_frame)
help_in_area = ttk.Combobox(main_frame, value=help_w_val)
link_e = Entry(main_frame, text="", state='readonly')
if stage == 1:
    survey_stage_1()
root.mainloop()
