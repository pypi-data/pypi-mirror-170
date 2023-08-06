""" Module containing main DLPOLY class.
"""

import subprocess
import os
import os.path
import sys
import shutil
from .new_control import (NewControl, is_new_control)
from .control import Control
from .config import Config
from .field import Field
from .statis import Statis
from .rdf import rdf
from .cli import get_command_args
from .utility import (copy_file, next_file, is_mpi)


class DLPoly:
    """ Main class of a DLPOLY runnable set of instructions """
    __version__ = "4.10"  # which version of dlpoly supports

    def __init__(self, control=None, config=None, field=None, statis=None, output=None,
                 dest_config=None, rdf=None, workdir=None, default_name=None, exe=None):
        # Default to having a control
        self.control = NewControl()
        self.config = None
        self.dest_config = dest_config
        self.default_name = default_name
        self.field = None
        self.statis = None
        self.rdf = None
        self.workdir = workdir
        self.exe = exe

        if default_name is None:
            self.default_name = "dlprun"

        if control is not None:
            self.load_control(control)
        if config is not None:
            self.load_config(config)
        if field is not None:
            self.load_field(field)
        if statis is not None:
            self.load_statis(statis)
        if rdf is not None:
            self.load_rdf(rdf)

        # Override output
        if output is not None:
            self.control.io_file_output = output

    def redir_output(self, direc=None):
        """ Redirect output to direc and update self for later parsing """
        if direc is None:
            direc = self.workdir

        # Set the path to be: direc/filename, stripping off all unnecessary pathing
        self.control.io_file_statis = os.path.abspath(
            os.path.join(direc, os.path.basename(self.control.io_file_statis)))
        self.control.io_file_revive = os.path.abspath(
            os.path.join(direc, os.path.basename(self.control.io_file_revive)))
        self.control.io_file_revcon = os.path.abspath(
            os.path.join(direc, os.path.basename(self.control.io_file_revcon)))

        if hasattr(self.control, 'traj') and not self.control.io_file_history:
            self.control.io_file_history = 'HISTORY'
        if self.control.io_file_history:
            self.control.io_file_history = os.path.abspath(
                os.path.join(direc, os.path.basename(self.control.io_file_history)))

        if self.control.io_file_historf:
            self.control.io_file_historf = os.path.abspath(
                os.path.join(direc, os.path.basename(self.control.io_file_historf)))

        if hasattr(self.control, 'restart') and not self.control.io_file_revold:
            self.control.io_file_revold = 'REVOLD'
        if self.control.io_file_revold:
            self.control.io_file_revold = os.path.abspath(
                os.path.join(direc, os.path.basename(self.control.io_file_revold)))

        if hasattr(self.control, 'rdf_print') and \
           self.control.rdf_print and \
           not self.control.io_file_rdf:
            self.control.io_file_rdf = 'RDFDAT'
        if self.control.io_file_rdf:
            self.control.io_file_rdf = os.path.abspath(
                os.path.join(direc, os.path.basename(self.control.io_file_rdf)))

        if hasattr(self.control, 'msdtmp') and not self.control.io_file_msd:
            self.control.io_file_msd = 'MSDTMP'
        if self.control.io_file_msd:
            self.control.io_file_msd = os.path.abspath(
                os.path.join(direc, os.path.basename(self.control.io_file_msd)))

    @staticmethod
    def _update_file(direc, file, dest_name=None):
        if dest_name is None:
            dest_name = os.path.basename(file)
        copy_file(file, os.path.join(direc, dest_name))
        return os.path.join(direc, os.path.basename(dest_name))

    def copy_input(self, direc=None):
        """ Copy input field and config to the working location """
        if direc is None:
            direc = self.workdir
        try:
            shutil.copy(self.fieldFile, direc)
        except shutil.SameFileError:
            pass

        if self.dest_config is None:
            self.configFile = self._update_file(direc, self.configFile)

        else:
            self.configFile = self._update_file(direc, self.configFile, self.dest_config)

        self.fieldFile = self._update_file(direc, self.fieldFile)

        if self.vdwFile:
            self.vdwFile = self._update_file(direc, self.vdwFile)
        if self.eamFile:
            self.eamFile = self._update_file(direc, self.eamFile)
        if self.control.io_file_tabbnd:
            self.control.io_file_tabbnd = self._update_file(direc, self.control.io_file_tabbnd)
        if self.control.io_file_tabang:
            self.control.io_file_tabang = self._update_file(direc, self.control.io_file_tabang)
        if self.control.io_file_tabdih:
            self.control.io_file_tabdih = self._update_file(direc, self.control.io_file_tabdih)
        if self.control.io_file_tabinv:
            self.control.io_file_tabinv = self._update_file(direc, self.control.io_file_tabinv)

    def write(self, control=True, config=True, field=True, prefix='', suffix=''):
        """ Write each of the components to file """
        if control:
            self.control.write(prefix+self.controlFile+suffix)
        if config and self.config:
            self.config.write(prefix+self.configFile+suffix)
        if field and self.field:
            self.field.write(prefix+self.fieldFile+suffix)

    def load_control(self, source=None):
        """ Load control file into class """
        if source is None:
            source = self.controlFile
        if os.path.isfile(source):
            if is_new_control(source):
                self.control = NewControl(source)
            else:
                self.control = Control(source).to_new()
            self.controlFile = source
        else:
            print(f"Unable to find file: {source}")

    def load_field(self, source=None):
        """ Load field file into class """
        if source is None:
            source = self.fieldFile
        if os.path.isfile(source):
            self.field = Field(source)
            self.fieldFile = source
        else:
            print(f"Unable to find file: {source}")

    def load_config(self, source=None):
        """ Load config file into class """
        if source is None:
            source = self.configFile
        if os.path.isfile(source):
            self.config = Config(source)
            self.configFile = source
        else:
            print(f"Unable to find file: {source}")

    def load_statis(self, source=None):
        """ Load statis file into class """
        if source is None:
            source = self.statisFile
        if os.path.isfile(source):
            self.statis = Statis(source)
            self.statisFile = source
        else:
            print(f"Unable to find file: {source}")

    def load_rdf(self, source=None):
        """ Load statis file into class """
        if source is None:
            source = self.rdfFile
        if os.path.isfile(source):
            self.rdf = rdf(source)
            self.rdfFile = source
        else:
            print(f"Unable to find file: {source}")

    @property
    def exe(self):
        """ executable name to be used to run DLPOLY"""
        return self._exe

    @exe.setter
    def exe(self, exe):
        """ set the executable name"""
        if exe is not None and os.path.isfile(exe):
            self._exe = exe
        else:
            if exe is None:  # user has not provided exe
                exe = "DLPOLY.Z"

            if "DLP_EXE" in os.environ:
                self._exe = os.environ["DLP_EXE"]
            elif shutil.which(exe):
                self._exe = shutil.which(exe)
            else:  # Assume in folder
                self._exe = exe
        try:
            proc = subprocess.run([exe, '-h'], capture_output=True)
            if f"Usage: {os.path.basename(exe)}" not in proc.stderr.decode(sys.stdout.encoding):
                print(f"{exe} is not DLPoly, run may not work")
        except FileNotFoundError:
            print(f"{exe} does not exist, run may not work")

    @property
    def controlFile(self):
        """ Path to control file """
        return self.control.io_file_control

    @controlFile.setter
    def controlFile(self, control):
        self.control.io_file_control = control

    @property
    def fieldFile(self):
        """ Path to field file """
        return self.control.io_file_field

    @fieldFile.setter
    def fieldFile(self, field):
        self.control.io_file_field = field

    @property
    def vdwFile(self):
        """ Path to TABLE for vdw file """
        return self.control.io_file_tabvdw

    @vdwFile.setter
    def vdwFile(self, vdw):
        self.control.io_file_tabvdw = vdw

    @property
    def eamFile(self):
        """ Path to TABEAM for eam file """
        return self.control.io_file_tabeam

    @eamFile.setter
    def eamFile(self, eam):
        self.control.io_file_tabeam = eam

    @property
    def configFile(self):
        """ Path to config file """
        return self.control.io_file_config

    @configFile.setter
    def configFile(self, config):
        self.control.io_file_config = config

    @property
    def statisFile(self):
        """ Path to statis file """
        return self.control.io_file_statis

    @statisFile.setter
    def statisFile(self, statis):
        self.control.io_file_statis = statis

    @property
    def rdfFile(self):
        """ Path to rdf file """
        return self.control.io_file_rdfFile

    @rdfFile.setter
    def rdfFile(self, rdf):
        self.control.io_file_rdfFile = rdf

    def run(self, executable=None, modules=(),
            numProcs=1, mpi='mpirun -n', outputFile=None):
        """ this is very primitive one allowing the checking
        for the existence of files and alteration of control parameters """

        # If we're defaulting to default name
        # Get last runname + 1 for this one
        if self.workdir is None:
            self.workdir = next_file(self.default_name)

        try:
            os.mkdir(self.workdir)
        except FileExistsError:
            print(f"Folder {self.workdir} exists, over-writing.")

        dlpexe = executable
        if executable is None:
            dlpexe = self.exe

        control_file = f"{self.workdir}/{os.path.basename(self.controlFile)}"
        self.copy_input()
        self.redir_output()
        self.control.write(control_file)

        if outputFile is None:
            outputFile = next_file(self.control.io_file_output)

        if is_mpi():
            from mpi4py.MPI import (COMM_WORLD, COMM_SELF)
            from mpi4py.MPI import Exception as MPIException

            error_code = 0
            if COMM_WORLD.Get_rank() == 0:
                try:
                    COMM_SELF.Spawn(dlpexe,
                                    [f"-c {control_file}", f"-o {outputFile}"],
                                    maxprocs=numProcs)
                except MPIException as err:
                    error_code = err.Get_error_code()

            error_code = COMM_WORLD.Bcast(error_code, 0)

        else:
            run_command = f"{dlpexe} -c {control_file} -o {outputFile}"

            if numProcs > 1:
                run_command = f"{mpi} {numProcs} {run_command}"

            if modules:
                load_mods = "module purge && module load " + modules
                with open("env.sh", 'w') as out_file:
                    out_file.write(load_mods+"\n")
                    out_file.write(run_command)
                    cmd = ['sh ./env.sh']
            else:
                cmd = [run_command]

            error_code = subprocess.call(cmd, shell=True)

        return error_code


def main():
    """ Run the main program """
    arg_list = get_command_args()
    dlp_run = DLPoly(control=arg_list.control, config=arg_list.config,
                     field=arg_list.field, statis=arg_list.statis,
                     workdir=arg_list.workdir)
    dlp_run.run(executable=arg_list.dlp)


if __name__ == "__main__":
    main()
