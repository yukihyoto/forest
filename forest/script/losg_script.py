
import forest
import base


class lo_freq_set(base.forest_script_base):
    method = 'LO_freq_set'
    ver = '2015.01.17'
    
    def run(self, freq, unit='GHz'):
        # Initialization Section
        # ======================
        
        # Check other operation
        # ---------------------
        self.check_other_operation()
        
        # Start operation
        # ---------------
        args = {'freq': freq, 'unit': unit}
        argstxt = str(args)
        self.operation_start(argstxt)
        
        # Print welcome message
        # ---------------------
        self.stdout.p('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        self.stdout.p('FOREST : Set 1st LOs Frequencies')
        self.stdout.p('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        self.stdout.p('ver.%s'%(self.ver))
        self.stdout.nextline()
        
        
        # Open devices
        # ------------
        self.stdout.p('Open Devices')
        self.stdout.p('============')
        
        lo_sg = self.open_lo_sg()
        
        self.stdout.nextline()
        
        
        # Operation Section
        # =================
        self.stdout.p('Set Frequencies')
        self.stdout.p('===============')
        
        self.stdout.write('1st LO SG : Set %.10f %s ... '%(freq, unit))
        lo_sg.freq_set(freq, unit)
        self.stdout.write('ok')
        self.stdout.nextline()
        
        # Finalization Section
        # ====================
        
        # Close devices
        # -------------
        self.stdout.p('Close Devices')
        self.stdout.p('=============')
        
        # TODO: implement close method.
        """
        lo_sg.close()
        """
        
        self.stdout.p('All devices are closed.')
        self.stdout.nextline()
        
        # Stop operation
        # --------------
        self.stdout.p('//// Operation is done. ////')
        self.operation_done()
        
        return

