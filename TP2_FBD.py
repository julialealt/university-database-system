import psycopg2
import numpy as np
DB_HOST = "200.129.44.249"
DB_NAME = "514094"
DB_USER = "514094"
DB_PASSWORD = "514094@fbd"
con = psycopg2.connect(host=DB_HOST, port="5432", database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cur = con.cursor()

import pandas as pd
from modulo import *

def menu():
    pd.set_option('display.max_columns', None)
    print('\n\033[95mSistema Universitário - SU\033[m')
  
    while True:

        print("\n")
        cabecalho('MENU PRINCIPAL')
        opc = menu_principal(['Inserir    (I)', 'Visualizar (V)', 'Remover    (R)', 'Atualizar  (A)', 'Sair       (S)'])

        opc = opc.upper()
        
        if opc == "I":
            print("\n")
            print('\n\033[95mInserir em: \033[m')
            print(linha())
            print("Aluno_faz           (1)")
            print("Alunos              (2)")
            print("Avaliação           (3)")
            print("Campi               (4)")
            print("Centros             (5)")
            print("Compoe              (6)")
            print("Cursa               (7)")
            print("Cursos              (8)")
            print("Disciplinas         (9)")
            print("Faz_avaliacao       (10)")
            print("Locais              (11)")
            print("Professores         (12)")
            print("Reitores            (13)")
            print("Tem_aula_em         (14)")
            print("Turmas              (15)")
            print(linha())

            opc_i = input("Digite uma opção: ")
            opc_i = opc_i.upper()
            print("\n")

            if opc_i == "1":
                rec = []
                rec.append(int(input("Digite o id do aluno: ")))
                rec.append(int(input("Digite o id da disciplina: ")))
                rec.append(input("Digite o semestre da turma: "))
                rec.append(int(input("Digite o id da turma: ")))

                try:
                    cur.execute('INSERT INTO aluno_faz VALUES (%s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3]))
                    con.commit()
                    print('\n\033[32mTupla inserida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "2":
                rec = []
                rec.append(input("Digite o nome do aluno: "))
                rec.append(input("Digite o sexo (F ou M ou O): "))
                rec.append(input("Digite o email: "))
                rec.append(input("Digite o endereço: "))
                rec.append(input("Digite a data de nascimento: "))
                rec.append(int(input("Digite a matrícula do aluno: ")))

                try:
                    cur.execute('INSERT INTO alunos VALUES (%s, %s, %s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5]))
                    con.commit()
                    print('\n\033[32mAluno inserido com sucesso! \033[m')
                except psycopg2.errors.UniqueViolation:
                    print('\n\033[31mERRO: A matrícula deve ser única. Este número de matrícula já existe.\033[m \n')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "3":
                rec = []
                rec.append(input("Digite a data da avaliação: "))
                rec.append(int(input("Digite o id da disciplina da avaliação: ")))
                rec.append(input("Digite o tipo da avaliação: "))

                try:
                    cur.execute('INSERT INTO avaliacao VALUES (%s, %s, %s) ', (rec[0], rec[1], rec[2]))
                    con.commit()
                    print('\n\033[32mAvaliação inserida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "4":
                rec = []
                print()
                rec.append(input("Digite o nome do campus: "))
                rec.append(input("Digite o município onde o campus se encontra: "))
                rec.append(int(input("Digite o id do campus: ")))
                id_prof = int(input("Digite o id do reitor atual: "))
                cur.execute('SELECT nome FROM professores WHERE id_prof = %s', (id_prof,))
                nome = cur.fetchone()
                rec.append(id_prof)
                rec.append(nome)

                try:
                    cur.execute('INSERT INTO campi VALUES (%s, %s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3], rec[4]))
                    con.commit()
                    print('\n\033[32mCampus inserido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "5":
                rec = []
                rec.append(input("Digite o nome do centro: "))
                rec.append(int(input("Digite o id do centro: ")))
                rec.append(int(input("Digite o id do campus: ")))
                rec.append(int(input("Digite o id do diretor do centro: ")))

                try:
                    cur.execute('INSERT INTO centros VALUES (%s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3]))
                    con.commit()
                    print('\n\033[32mCentro inserido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "6":
                rec = []
                rec.append(int(input("Digite o id do professor: ")))
                rec.append(int(input("Digite o id do curso: ")))

                try:
                    cur.execute('INSERT INTO compoe VALUES (%s, %s)', (rec[0], rec[1]))
                    con.commit()
                    print('\n\033[32mTupla inserida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "7":
                rec = []
                rec.append(int(input("Digite o id do aluno: ")))
                rec.append(int(input("Digite o id do curso: ")))

                try:
                    cur.execute('INSERT INTO cursa VALUES (%s, %s) ', (rec[0], rec[1]))
                    con.commit()
                    print('\n\033[32mTupla inserida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "8":
                rec = []
                rec.append(input("Digite o nome do curso: "))
                rec.append(input("Digite a carga horária do curso: "))
                rec.append(int(input("Digite o id do curso: ")))
                rec.append(int(input("Digite o id do centro do curso: ")))
                rec.append(int(input("Digite o id do coordenador do curso: ")))

                try:
                    cur.execute('INSERT INTO cursos VALUES (%s, %s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3], rec[4]))
                    con.commit()
                    print('\n\033[32mCurso inserido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "9":
                rec = []
                rec.append(input("Digite o nome da disciplina: "))
                rec.append(input("Digite a ementa: "))
                rec.append(input("Digite a carga horária: "))
                rec.append(int(input("Digite o id da disciplina: ")))
                rec.append(int(input("Digite o id do professor: ")))

                try:
                    cur.execute('INSERT INTO disciplinas VALUES (%s, %s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3], rec[4]))
                    con.commit()
                    print('\n\033[32mDisciplina inserida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

          
            elif opc_i == "10":
                rec = []
                rec.append(int(input("Digite a matricula do aluno: ")))
                rec.append(int(input("Digite a nota do aluno na avaliação: ")))
                rec.append(int(input("Digite o id da disciplina: ")))
                rec.append(input("Digite a data da avaliação: "))

                try:
                    cur.execute('INSERT INTO faz_avaliacao VALUES (%s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3]))
                    con.commit()
                    print('\n\033[32mTupla inserida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "11":
                rec = []
                rec.append(input("Digite o nome do local: "))
                rec.append(input("Digite o tipo do local: "))
                rec.append(input("Digite a descrição do local: "))
                rec.append(int(input("Digite o id do local: ")))
                rec.append(int(input("Digite o id do centro que o local faz parte: ")))
                rec.append(int(input("Digite a lotação do local: ")))
                rec.append(int(input("Digite o bloco o qual o local faz parte: ")))

                try:
                    cur.execute('INSERT INTO locais VALUES (%s, %s, %s, %s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6]))
                    con.commit()
                    print('\n\033[32mLocal inserido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "12":
                rec = []
                rec.append(input("Digite o nome do professor: "))
                rec.append(input("Digite o email: "))
                rec.append(input("Digite o sexo (F ou M ou O): "))
                rec.append(int(input("Digite o id do professor: ")))
                rec.append(input("Digite o grau de formação: "))
                rec.append(0)
                rec.append(0)
                rec.append(input("Digite a data de nascimento: "))
                resp_reitor = input("O(A) professor(a) é reitor(a)? ")
                resp_reitor = resp_reitor.upper()

                try:
                    cur.execute('INSERT INTO professores VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7]))
                    con.commit()
                    cur.execute('INSERT INTO compoe VALUES (%s, %s) ', (rec[3], None))
                    con.commit()
                    if resp_reitor == "SIM" or resp_reitor == "S" or resp_reitor == "SS":
                        rec.append(input("Digite a data de admissão do reitor: "))
                        cur.execute('INSERT INTO reitores VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8]))
                        con.commit()
                    print('\n\033[32mProfessor inserido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "13":
                id_prof = (int(input("Digite o id do professor: ")))
                data_admissao = (input("Digite a data de admissão do reitor: "))

                try:
                    cur.execute('SELECT nome FROM professores WHERE id_prof = %s', (id_prof,))
                    nome = cur.fetchone()
                    cur.execute('SELECT email FROM professores WHERE id_prof = %s', (id_prof,))
                    email = cur.fetchone()
                    cur.execute('SELECT sexo FROM professores WHERE id_prof = %s', (id_prof,))
                    sexo = cur.fetchone()
                    cur.execute('SELECT grau_formacao FROM professores WHERE id_prof = %s', (id_prof,))
                    grau_formacao = cur.fetchone()
                    cur.execute('SELECT coordenador FROM professores WHERE id_prof = %s', (id_prof,))
                    coord = cur.fetchone()
                    cur.execute('SELECT diretor FROM professores WHERE id_prof = %s', (id_prof,))
                    diretor = cur.fetchone()
                    cur.execute('SELECT data_de_nascimento FROM professores WHERE id_prof = %s', (id_prof,))
                    data_de_nasc = cur.fetchone()

                    cur.execute('INSERT INTO reitores VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ', (nome, email, sexo, id_prof, grau_formacao, coord, diretor, data_de_nasc, data_admissao))
                    print('\n\033[32mReitor inserido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "14":
                rec = []
                rec.append(int(input("Digite o id do local: ")))
                rec.append(int(input("Digite o id da turma: ")))
                rec.append(input("Digite o semestre da turma (no formato ano.semestre): "))

                try:
                    cur.execute('INSERT INTO tem_aula_em VALUES (%s, %s, %s) ', (rec[0], rec[1], rec[2]))
                    con.commit()
                    print('\n\033[32mTupla inserida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                

            elif opc_i == "15":
                rec = []
                rec.append(input("Digite o nome da turma: "))
                rec.append(input("Digite o estado (ABERTA ou CONCLUÍDA): "))
                rec.append(input("Digite os dias da semana: "))
                rec.append(int(input("Digite o id da disciplina ministrada nessa turma: ")))
                rec.append(int(input("Digite o número de vagas: ")))
                rec.append(int(input("Digite o número de matriculados: ")))
                rec.append(input("Digite o semestre da turma (no formato ano.semestre): "))
                rec.append(int(input("Digite o id da turma: ")))
                rec.append(input("Digite o horário: "))

                try:
                    cur.execute('INSERT INTO turmas VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8]))
                    con.commit()
                    print('\n\033[32mTurma inserida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
            

            else:
                print('\n\033[31mERRO: Número de tabela digitado não existe.\033[m \n')

                

        elif opc == "V":
            print("\n")
            print('\n\033[95mVisualizar de: \033[m')
            print(linha())
            print("Aluno_faz                                (1)")
            print("Alunos                                   (2)")
            print("Avaliação                                (3)")
            print("Campi                                    (4)")
            print("Centros                                  (5)")
            print("Compoe                                   (6)")
            print("Cursa                                    (7)")
            print("Cursos                                   (8)")
            print("Disciplinas                              (9)")
            print("Faz_avaliacao                            (10)")
            print("Locais                                   (11)")
            print("Professores                              (12)")
            print("Reitores                                 (13)")
            print("Tem_aula_em                              (14)")
            print("Turmas                                   (15)")
            print("Média de uma turma concluída             (16)")
            print("Turmas de determinado semestre           (17)")
            print("Locais de determinado bloco              (18)")
            print("Turmas de determinado local              (19)")
            print("Médias de aluno de determinada matrícula (20)")
            print(linha())

            opc_i = input("Digite uma opção: ")
            opc_i.upper()
            print("\n")

            if opc_i == "1":
                df = pd.read_sql('SELECT * FROM aluno_faz', con)
                print(df)
                con.commit()

            elif opc_i == "2":
                df = pd.read_sql('SELECT * FROM alunos', con)
                print(df)
                con.commit()

            elif opc_i == "3":
                df = pd.read_sql('SELECT * FROM avaliacao', con)
                print(df)
                con.commit()

            elif opc_i == "4":
                df = pd.read_sql('SELECT * FROM campi', con)
                print(df)
                con.commit()

            elif opc_i == "5":
                df = pd.read_sql('SELECT * FROM centros', con)
                print(df)
                con.commit()

            elif opc_i == "6":
                df = pd.read_sql('SELECT * FROM compoe', con)
                print(df)
                con.commit()

            elif opc_i == "7":
                df = pd.read_sql('SELECT * FROM cursa', con)
                print(df)
                con.commit()

            elif opc_i == "8":
                df = pd.read_sql('SELECT * FROM cursos', con)
                print(df)
                con.commit()

            elif opc_i == "9":
                df = pd.read_sql('SELECT * FROM disciplinas', con)
                print(df)
                con.commit()

            elif opc_i == "10":
                df = pd.read_sql('SELECT * FROM faz_avaliacao', con)
                print(df)
                con.commit()

            elif opc_i == "11":
                df = pd.read_sql('SELECT * FROM locais', con)
                print(df)
                con.commit()

            elif opc_i == "12":
                df = pd.read_sql('SELECT * FROM professores', con)
                print(df)
                con.commit()

            elif opc_i == "13":
                df = pd.read_sql('SELECT * FROM reitores', con)
                print(df)
                con.commit()

            elif opc_i == "14":
                df = pd.read_sql('SELECT * FROM tem_aula_em', con)
                print(df)
                con.commit()

            elif opc_i == "15":
                df = pd.read_sql('SELECT * FROM turmas', con)
                print(df)
                con.commit()

            elif opc_i == "16":
                id_t = int(input("digite o id da turma desejada: "))
                semestre = input("Digite o semestre desejado: ")
                str = "CONCLUIDA"
                sql_query = 'SELECT AVG(faz_avaliacao.nota), turmas.nome FROM turmas, aluno_faz, faz_avaliacao \
                            WHERE turmas.id_turma = %s AND turmas.semestre = %s \
                                AND aluno_faz.id_turma = turmas.id_turma AND turmas.estado = %s \
                                AND aluno_faz.semestre = turmas.semestre AND aluno_faz.id_disc = faz_avaliacao.id_disc \
                            GROUP BY faz_avaliacao.matricula, turmas.nome'
                cur.execute(sql_query, (id_t, semestre, str))
                data = cur.fetchall()
                print(pd.DataFrame(np.array(data)))


            elif opc_i == "17":
                sem = input("Digite o semestre desejado: ")
                sql_query = 'SELECT * from turmas WHERE turmas.semestre = %s'
                cur.execute(sql_query, (sem,))
                data = cur.fetchall()
                print(pd.DataFrame(np.array(data)))

            elif opc_i == "18":
                blo = int(input("Digite o bloco desejado: "))
                sql_query = 'SELECT * from locais WHERE locais.bloco = %s'
                cur.execute(sql_query, (blo,))
                data = cur.fetchall()
                print(pd.DataFrame(np.array(data)))

            elif opc_i == "19":
                loc = int(input("Digite o id do local desejado: "))
                sql_query = 'SELECT turmas.nome, disciplinas.nome, turmas.horario \
                            FROM locais, turmas, tem_aula_em, disciplinas \
                            WHERE locais.id_local = %s AND tem_aula_em.id_local = locais.id_local AND tem_aula_em.id_turma= turmas.id_turma \
                            AND disciplinas.id_disc = turmas.id_disc'
                cur.execute(sql_query, (loc,))
                data = cur.fetchall()
                print(pd.DataFrame(np.array(data)))
            
            elif opc_i == "20":
                mat = int(input("Digite a matrícula do aluno desejado: "))
                sql_query = 'SELECT AVG(faz_avaliacao.nota), disciplinas.nome FROM faz_avaliacao, disciplinas \
                            WHERE matricula = %s AND faz_avaliacao.id_disc = disciplinas.id_disc \
                            GROUP BY faz_avaliacao.id_disc, disciplinas.id_disc'

                cur.execute(sql_query, (mat,))
                data = cur.fetchall()
                print(pd.DataFrame(np.array(data)))


            else:
                print('\n\033[31mERRO: Número de tabela digitado não existe.\033[m \n')


        elif opc == "R":
            print("\n")
            print('\n\033[95mRemover de: \033[m')
            print(linha())
            print("Aluno_faz           (1)")
            print("Alunos              (2)")
            print("Avaliação           (3)")
            print("Campi               (4)")
            print("Centros             (5)")
            print("Compoe              (6)")
            print("Cursa               (7)")
            print("Cursos              (8)")
            print("Disciplinas         (9)")
            print("Faz_avaliacao       (10)")
            print("Locais              (11)")
            print("Professores         (12)")
            print("Reitores            (13)")
            print("Tem_aula_em         (14)")
            print("Turmas              (15)")
            print(linha())

            opc_i = input("Digite uma opção: ")
            opc_i.upper()
            print("\n")

            if opc_i == "1":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_aluno = int(input("Digite a matrícula do aluno: "))
                id_disc = int(input("Digite o id da disciplina: "))
                semestre = input("Digite o semestre da turma: ")

                try:
                    cur.execute('DELETE FROM aluno_faz WHERE id_aluno = %s AND id_disc = %s AND semestre = %s', (id_aluno, id_disc, semestre))
                    con.commit()
                    print('\n\033[32mTupla removida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "2":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                matricula = int(input("Digite a matrícula do aluno: "))

                try:
                    cur.execute('DELETE FROM alunos WHERE matricula = %s', (matricula,))
                    con.commit()
                    print('\n\033[32mAluno removido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "3":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_disc = int(input("Digite o id da disciplina: "))
                data = input("Digite a data da avaliação: ")

                try:
                    cur.execute('DELETE FROM avaliacao WHERE id_disc = %s AND data = %s', (id_disc, data))
                    con.commit()
                    print('\n\033[32mAvaliação removida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "4":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_campus = int(input("Digite o id do campus: "))

                try:
                    cur.execute('DELETE FROM campi WHERE id_campus = %s', (id_campus,))
                    con.commit()
                    print('\n\033[32mCampus removido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "5":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_centro = int(input("Digite o id do centro: "))

                try:
                    cur.execute('DELETE FROM centros WHERE id_centro = %s', (id_centro,))
                    con.commit()
                    print('\n\033[32mCentro removido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "6":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_prof = int(input("Digite o id do professor: "))

                try:
                    cur.execute('DELETE FROM compoe WHERE id_prof = %s', (id_prof,))
                    con.commit()
                    print('\n\033[32mTupla removida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "7":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_aluno = int(input("Digite a matrícula do aluno: "))
                id_curso = int(input("Digite o id do curso: "))

                try:
                    cur.execute('DELETE FROM cursa WHERE id_aluno = %s AND id_curso = %s', (id_aluno, id_curso))
                    con.commit()
                    print('\n\033[32mTupla removida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "8":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_curso = int(input("Digite o id do curso: "))

                try:
                    cur.execute('DELETE FROM cursos WHERE id_curso = %s', (id_curso,))
                    con.commit()
                    print('\n\033[32mCurso removido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "9":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_disc = int(input("Digite o id da disciplina: "))

                try:
                    cur.execute('DELETE FROM disciplinas WHERE id_disc = %s', (id_disc,))
                    con.commit()
                    print('\n\033[32mDisciplina removida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "10":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_aluno = int(input("Digite a matrícula do aluno: "))
                id_disc = int(input("Digite o id da disciplina: "))
                data = input("Digite a data da avaliação: ")

                try:
                    cur.execute('DELETE FROM faz_avaliacao WHERE matricula = %s AND id_disc = %s AND data = %s', (id_aluno, id_disc, data))
                    con.commit()
                    print('\n\033[32mTupla removida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "11":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_local = int(input("Digite o id do local: "))

                try:
                    cur.execute('DELETE FROM locais WHERE id_local = %s', (id_local,))
                    con.commit()
                    print('\n\033[32mLocal removido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "12":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_prof = int(input("Digite o id do professor: "))

                try:
                    cur.execute('DELETE FROM professores WHERE id_prof = %s', (id_prof,))
                    con.commit()
                    cur.execute('DELETE FROM reitores WHERE id_prof = %s', (id_prof,))
                    con.commit()
                    print('\n\033[32mProfessor removido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "13":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_reitor = int(input("Digite o id do reitor: "))

                try:
                    cur.execute('DELETE FROM reitores WHERE id_prof = %s', (id_reitor,))
                    con.commit()
                    print('\n\033[32mReitor removido com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "14":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_local = int(input("Digite o id do local: "))
                id_turma = int(input("Digite o id da turma: "))
                semestre = input("Digite o semestre da turma: ")

                try:
                    cur.execute('DELETE FROM tem_aula_em WHERE id_local = %s AND id_turma = %s AND semestre = %s', (id_local, id_turma, semestre))
                    con.commit()
                    print('\n\033[32mTupla removida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "15":
                print('\033[95mDigite a chave primária da tupla que será removida: \033[m')
                id_turma = int(input("Digite o id da turma: "))
                semestre = input("Digite o semestre da turma (no formato ano.semestre): ")

                try:
                    cur.execute('DELETE FROM turmas WHERE id_turma = %s AND semestre = %s', (id_turma, semestre))
                    con.commit()
                    print('\n\033[32mTurma removida com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
            

            else:
                print('\n\033[31mERRO: Número de tabela digitado não existe.\033[m \n')




        elif opc == "A":
            print("\n")
            print('\n\033[95mAtualizar em: \033[m')
            print(linha())
            print("Aluno_faz           (1)")
            print("Alunos              (2)")
            print("Avaliação           (3)")
            print("Campi               (4)")
            print("Centros             (5)")
            print("Compoe              (6)")
            print("Cursa               (7)")
            print("Cursos              (8)")
            print("Disciplinas         (9)")
            print("Faz_avaliacao       (10)")
            print("Locais              (11)")
            print("Professores         (12)")
            print("Reitores            (13)")
            print("Tem_aula_em         (14)")
            print("Turmas              (15)")
            print(linha())

            opc_i = input("Digite uma opção: ")
            opc_i.upper()
            print("\n")

            if opc_i == "1":
                print('\n\033[31mNada a ser atualizado nesta tabela.\033[m \n')


            elif opc_i == "2":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id = int(input("Digite a matrícula do aluno da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome do aluno: "))
                rec.append(input("Digite o sexo (F ou M ou O): "))
                rec.append(input("Digite o email: "))
                rec.append(input("Digite o endereço: "))
                rec.append(input("Digite a data de nascimento: "))
                rec.append(id)

                try:
                    cur.execute('UPDATE alunos SET nome= %s,sexo= %s,email= %s,endereco= %s,data_de_nascimento= %s,matricula= %s WHERE matricula = %s', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], id))
                    con.commit()
                    print('\n\033[32mAluno atualizado com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
                
                
            elif opc_i == "3":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_disc = int(input("Digite o id da disciplina da tupla que será atualizada: "))
                data = input("Digite a data da tupla que será atualizada: ")

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(data)
                rec.append(id_disc)
                rec.append(input("Digite o tipo da avaliação: "))

                try:
                    cur.execute('UPDATE avaliacao SET data= %s,id_disc= %s,tipo= %s WHERE id_disc = %s AND data = %s', (rec[0], rec[1], rec[2], id_disc, data))
                    con.commit()
                    print('\n\033[32mAvaliação atualizada com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "4":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_campus = int(input("Digite o id do campus da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome do campus: "))
                rec.append(input("Digite o município: "))
                rec.append(id_campus)
                id_prof = int(input("Digite o id do reitor atual: "))
                cur.execute('SELECT nome FROM professores WHERE id_prof = %s', (id_prof,))
                nome = cur.fetchone()
                rec.append(id_prof)
                rec.append(nome)

                try:
                    cur.execute('UPDATE campi SET nome= %s,municipio= %s,id_campus= %s,id_reitor_atual= %s,nome_reitor_atual = %s WHERE id_campus = %s', (rec[0], rec[1], rec[2], rec[3], rec[4], id_campus))
                    con.commit()
                    print('\n\033[32mCampus atualizado com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "5":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_centro = int(input("Digite o id do centro da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome do centro: "))
                rec.append(id_centro)
                rec.append(int(input("Digite o id do campus no qual o centro se encontra: ")))
                rec.append(int(input("Digite o id do diretor do centro: ")))

                try:
                    cur.execute('UPDATE centros SET nome= %s,id_centro= %s,id_campus= %s,id_diretor= %s WHERE id_centro = %s ', (rec[0], rec[1], rec[2], rec[3], id_centro))
                    con.commit()
                    print('\n\033[32mCentro atualizado com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')

                
            elif opc_i == "6":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_prof = int(input("Digite o id do professor da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(int(input("Digite o id do curso o qual o professor faz parte: ")))

                try:
                    cur.execute('UPDATE compoe SET id_curso= %s WHERE id_prof = %s ', (rec[0], id_prof))
                    con.commit()
                    print('\n\033[32mTupla atualizada com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "7":
                print('\n\033[31mNada a ser atualizado nesta tabela.\033[m \n')


            elif opc_i == "8":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_curso = int(input("Digite o id do curso da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome do curso: "))
                rec.append(input("Digite a carga horária: "))
                rec.append(id_curso)
                rec.append(int(input("Digite o id do centro do curso: ")))
                rec.append(int(input("Digite o id do coordenador do curso: ")))

                try:
                    cur.execute('UPDATE cursos SET nome= %s,carga_horaria= %s,id_curso= %s,id_centro_do_curso= %s, id_coordenador= %s WHERE id_curso = %s ', (rec[0], rec[1], rec[2], rec[3], rec[4], id_curso))
                    con.commit()
                    print('\n\033[32mCurso atualizado com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "9":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_disc = int(input("Digite o id da disciplina da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome da disciplina: "))
                rec.append(input("Digite a ementa: "))
                rec.append(input("Digite a carga horária: "))
                rec.append(id_disc)
                rec.append(int(input("Digite o id do professor: ")))

                try:
                    cur.execute('UPDATE disciplinas SET nome= %s,ementa= %s,carga_horaria= %s,id_disc= %s, id_professor= %s WHERE id_disc = %s ', (rec[0], rec[1], rec[2], rec[3], rec[4], id_disc))
                    con.commit()
                    print('\n\033[32mDisciplina atualizada com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "10":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_aluno = int(input("Digite a matrícula do aluno da tupla que será atualizada: "))
                id_disc = int(input("Digite o id da disciplina da tupla que será atualizada: "))
                data = input("Digite a data da tupla que será atualizada: ")

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(id_aluno)
                rec.append(int(input("Digite a nota: ")))
                rec.append(id_disc)
                rec.append(data)

                try:
                    cur.execute('UPDATE faz_avaliacao SET matricula= %s,nota= %s,id_disc= %s,data= %s WHERE matricula = %s AND id_disc = %s AND data = %s', (rec[0], rec[1], rec[2], rec[3], id_aluno, id_disc, data))
                    con.commit()
                    print('\n\033[32mTupla atualizada com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "11":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_local = int(input("Digite o id do local da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome do local: "))
                rec.append(input("Digite o tipo do local: "))
                rec.append(input("Digite a descrição do local: "))
                rec.append(id_local)
                rec.append(int(input("Digite o id do centro que o local faz parte: ")))
                rec.append(int(input("Digite a lotação do local: ")))
                rec.append(int(input("Digite o bloco o qual o local faz parte: ")))

                try:
                    cur.execute('UPDATE locais SET nome= %s,tipo= %s,descricao= %s, id_local= %s, id_centro= %s, lotacao= %s, bloco= %s WHERE id_local = %s ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], id_local))
                    con.commit()
                    print('\n\033[32mLocal atualizado com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "12":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_prof = int(input("Digite o id do professor da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome do professor: "))
                rec.append(input("Digite o email: "))
                rec.append(input("Digite o sexo (F ou M ou O): "))
                rec.append(id_prof)
                rec.append(input("Digite o grau de formação: "))
                cur.execute('SELECT coordenador FROM professores WHERE id_prof = %s', (id_prof,))
                coordenador = cur.fetchone()
                cur.execute('SELECT diretor FROM professores WHERE id_prof = %s', (id_prof,))
                diretor = cur.fetchone()
                rec.append(coordenador)
                rec.append(diretor)
                rec.append(input("Digite a data de nascimento: "))
                id_curso = int(input("Digite o id do curso o qual o professor faz parte: "))

                try:
                    cur.execute('UPDATE professores SET nome= %s,email= %s,sexo= %s,id_prof= %s,grau_formacao= %s,coordenador= %s,diretor= %s, data_de_nascimento= %s WHERE id_prof = %s ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], id_prof))
                    con.commit()
                    cur.execute('UPDATE reitores SET nome= %s,email= %s,sexo= %s,id_prof= %s,grau_formacao= %s,coordenador= %s,diretor= %s, data_de_nascimento= %s WHERE id_prof = %s ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], id_prof))
                    con.commit()
                    cur.execute('UPDATE compoe SET id_prof= %s, id_curso= %s WHERE id_prof = %s', (id_prof, id_curso, id_prof))
                    con.commit()
                    print('\n\033[32mProfessor atualizado com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "13":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_reitor = int(input("Digite o id do reitor da tupla que será atualizada: "))

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome do reitor: "))
                rec.append(input("Digite o email: "))
                rec.append(input("Digite o sexo (F ou M ou O): "))
                rec.append(id_reitor)
                rec.append(input("Digite o grau de formação: "))
                cur.execute('SELECT coordenador FROM professores WHERE id_prof = %s', (id_reitor,))
                coordenador = cur.fetchone()
                cur.execute('SELECT diretor FROM professores WHERE id_prof = %s', (id_reitor,))
                diretor = cur.fetchone()
                rec.append(coordenador)
                rec.append(diretor)
                rec.append(input("Digite a data de nascimento: "))
                rec.append(input("Digite a data de admissão: "))

                try:
                    cur.execute('UPDATE reitores SET nome= %s,email= %s,sexo= %s,id_prof= %s,grau_formacao= %s,coordenador= %s,diretor= %s, data_de_nascimento= %s, data_de_admissao= %s WHERE id_prof = %s ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], id_reitor))
                    con.commit()
                    cur.execute('UPDATE professores SET nome= %s,email= %s,sexo= %s,id_prof= %s,grau_formacao= %s,coordenador= %s,diretor= %s, data_de_nascimento= %s WHERE id_prof = %s ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], id_reitor))
                    con.commit()
                    print('\n\033[32mReitor atualizado com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')


            elif opc_i == "14":
                print('\n\033[31mNada a ser atualizado nesta tabela.\033[m \n')


            elif opc_i == "15":
                rec = []
                print('\033[95mDigite a chave primária: \033[m')
                id_turma = int(input("Digite o id da turma da tupla que será atualizada: "))
                semestre = input("Digite o semestre da turma (no formato ano.semestre): ")

                print('\n\033[95mDigite os novos dados: \033[m')
                rec.append(input("Digite o nome da turma: "))
                rec.append(input("Digite o estado (ABERTA ou CONCLUÍDA): "))
                rec.append(input("Digite os dias da semana: "))
                rec.append(int(input("Digite o id da disciplina: ")))
                cur.execute('SELECT num_vagas FROM turmas WHERE id_turma = %s AND semestre = %s ', (id_turma, semestre))
                num_vagas = cur.fetchone()
                cur.execute('SELECT num_matriculados FROM turmas WHERE id_turma = %s AND semestre = %s ', (id_turma, semestre))
                num_matriculados = cur.fetchone()
                rec.append(num_vagas)
                rec.append(num_matriculados)
                rec.append(semestre)
                rec.append(id_turma)
                rec.append(input("Digite o horário: "))

                try:
                    cur.execute('UPDATE turmas SET nome= %s,estado= %s,dias_semana= %s, id_disc= %s, num_vagas= %s, num_matriculados= %s, semestre= %s,id_turma= %s,horario= %s WHERE id_turma = %s AND semestre = %s ', (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], id_turma, semestre))
                    con.commit()
                    print('\n\033[32mTurma atualizada com sucesso! \033[m')
                except Exception as e: 
                    print('\n')
                    print(f'\n\033[31m{e}\033[m \n')
            

            else:
                print('\n\033[31mERRO: Tabela digitado não existe.\033[m \n')
                

        elif opc == "S":
            print("\n")
            print(linha())
            print('\033[33m       Encerrando o programa... Até logo! \033[m')
            print(linha())
            print("\n")
            break

menu()
con.close()
