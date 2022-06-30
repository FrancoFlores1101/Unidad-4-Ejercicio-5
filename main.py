from RepositorioPacientes import RespositorioPacientes
from claseVista import VistaPacientes
from Controler import ControladorPacientes
from ObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder('pacientes.json')
    repo=RespositorioPacientes(conn)
    vista=VistaPacientes()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()
