from random import *

# generates questions and answers on every instanciation
class Questioner():
    def __init__(self):
        questions = [self.question_pipe, self.question_time_performance, self.question_stack_pointer, self.question_branching]
        question = questions[randint(0, len(questions)-1)]
        self.text, self.true_answer = question()
    
    def question_pipe(self):
        computer_speed = round(uniform(2, 5), 2)
        answer_true = str(round(computer_speed * 1000 / 1))
        question_text = "Arvuta käskude läbilaskevõime viieastmelise toruga arvutis, kui selle arvuti taktsagedus on " + str(computer_speed) + " GHz ja toru töötab ideaalses töörežiimis üks käsk iga takti kohta. Vastus esita ühikutes MIPS (kirjuta arv ilma ühikuta)."
        return (question_text, answer_true)
    
    def question_time_performance(self):
        N = randint(50, 200)
        S = round(uniform(1, 3), 1)
        F = round(uniform(3, 6), 2)
        answer_true = str(round(N * S / F, 1))
        question_text = "Leia aeg, mis kulub masinkoodil " + str(N) + " käsu käivitamiseks, kui arvuti taktsagedus on " + str(F) + " GHz ja keskmiselt kulub ühe masinkoodi käsu täitmiseks " + str(S) + " sammu. Vastus esita nanosekundites ühe komakoha täpsusega (kirjuta ainult arv)."
        return (question_text, answer_true)
    
    def question_stack_pointer(self):
        stack_pointer = 1880
        n_parameters = randint(2, 8)
        n_local_variables = randint(2, 8)
        n_registers = randint(3, 10)
        word_length = 2 ** randint(3, 6)
        answer_true = str(round(stack_pointer - (n_parameters + 1 + 1 + n_local_variables + n_registers) * (word_length / 8))) 
        question_text = "Stack pointer viitab mälupesale " + str(stack_pointer) + " Programm lisab pinusse alamprogrammi jaoks " + str(n_parameters) + " parameetrit, kutsub välja alamprogrammi. Alamprogramm salvestab pinus tagasipöördumise aadressi, frame pointeri sisu, " + str(n_local_variables) + " lokaalmuutujat ja " + str(n_registers) + " registri sisu. Milline on stack pointeri väärtus peale nimetet operatsioonide sooritamist, kui sõna pikkuseks on " + str(word_length) + " bitti ja tegemist on bait-adresseeritava mäluga (kirjuta ainult arv)?"
        return (question_text, answer_true)
    
    def question_branching(self):
        branch_commands = round(random() * 100)
        delay_slot_fill = round(random() * 100)
        answer_true = str(round((100 + branch_commands) / (100 + branch_commands - (branch_commands * delay_slot_fill) / 100), 2))
        question_text = "Meie programmi dünaamilises töövoos on " + str(branch_commands) + "% hargnemise käske. Kasutatakse hargnemise ajatamist (delayed branching) ühe ajatuspesaga (delay slot). Arvuta, mitu korda kiireneb sellise programmi käivitamine, kui kompilaator suudab ajatuspesa täita " + str(delay_slot_fill) + "% juhtudest (võrreldes ajatuspesa kasutamata jätmise olukorraga)? Vastus esita kahe komakoha täpsusega."
        return (question_text, answer_true)

    def answer_question(self, user_answer):
        return user_answer == self.true_answer
