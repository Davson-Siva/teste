import mysql.connector
from mysql.connector import Error
import time
from GENERIC_FUNC import *

def conectar_bd():
    try:
        ultra_debug("conectar_bd() - INICIO")
        banco = mysql.connector.connect(
            #host=,
            #user=,
            #passwd= ,
            #database = "consig",
            #auth_plugin='mysql_native_password'
        )
        if banco.is_connected():
            db_info = banco.get_server_info()
            ultra_debug("Conectado ao servidor MySQL")
            ultra_debug("conectado")
            return banco

        else:
            return False
    except Error as erro:
        ultra_debug(erro)
def consulta_chamados():
    ultra_debug("consulta_chamados() - INICIO")
    try:
        con = conectar_bd()
        if con != False:
            consulta_sql = "SELECT chamados.id, chamados.cpf_cliente, base_clientes.prec_cp FROM chamados LEFT JOIN base_clientes ON base_clientes.cpf = chamados.cpf_cliente WHERE chamados.status = 0 AND chamados.chamado_motivo_id = 24 and base_clientes.base = 'EXERCITO';"
            cursor = con.cursor()
            cursor.execute(consulta_sql)
            chamados = cursor.fetchall()
            ultra_debug("CONSULTA FINALIZADA")
            return chamados
        else:
            ultra_debug("Não estamos conectados ao banco de dados")
            return False
    except:
        ultra_debug("Não foi possível finalizar a consulta de chamados;")
        



def responde_chamado(id_do_chamado, senha_eb):
    ultra_debug("responde_chamado(id_do_chamado, senha_eb) - INICIO")
    try:
        con = conectar_bd()
        if con != False:
            consulta_sql = "INSERT INTO chamado_registros (chamado_id, mensagem, created_at, updated_at) VALUES (" + id_do_chamado + ", '" + senha_eb + "', NOW(), NOW());"
            ultra_debug(consulta_sql)
            cursor = con.cursor()
            ultra_debug("criei o cursor")
            cursor.execute(consulta_sql)
            con.commit()
            ultra_debug("CHAMADO RESPONDIDO")
            return True
    except:
        ultra_debug("Falha ao responder chamadado (banco de dados")
        return False
        
def atualizar_chamado(id_do_chamado):
    id_do_chamado = str(id_do_chamado)
    ultra_debug("atualizar_chamado(id_do_chamado) - INICIO")
    try:
        con = conectar_bd()
        consulta_sql = "UPDATE chamados SET status = 2, resolvido = 0, updated_at = NOW() WHERE id = " + id_do_chamado + ";"
        ultra_debug(consulta_sql)
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        con.commit()
        ultra_debug("CHAMADO ATUALIZADO")
        return True
    except:
        ultra_debug("falaha ao atualizar o chamado")
        return False

def excluir_senha(prec_cp):
    ultra_debug("excluir_senha(prec_cp) - INICIO")
    try:
        con = conectar_bd()
        consulta_sql = "DELETE FROM base_senhas WHERE prec_cp = '" + prec_cp + "';"
        ultra_debug(consulta_sql)
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        con.commit()
        ultra_debug("senha excluida")
        return True
    except:
        ultra_debug("falaha ao atualizar o chamado")
        return False

def atualiza_senha(senha_eb, prec_cp):
    ultra_debug("atualiza_senha(senha_eb, prec_cp) - INICIO")
    senha_eb = str(senha_eb)
    prec_cp = str(prec_cp)
    try:
        con = conectar_bd()
        consulta_sql = "INSERT INTO base_senhas (prec_cp, senha) VALUES ('" + prec_cp + "','" + senha_eb + "');"
        ultra_debug(consulta_sql)
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        con.commit()
        ultra_debug("senha atualizada")
        return True
    except:
        ultra_debug("falha ao atualizar o chamado")
        return False


#"""host: 165.227.24.218
 #   database: consig
  #  username: robo
   # password: yLaItfqa5k1y
    #ssl_mode: :disabled
    #sslverify: false"""
