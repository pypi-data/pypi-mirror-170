# -*- coding:utf-8 -*-

'''
Created on 2021.12
@author: tanjiaxi
'''

import os
import sys
import ctypes
import _ctypes
import struct

from . import structs
from . import errors


def output_func(msg):
    print(msg.decode())
    

class CKLink(object):
    """Python interface for the T-HEAD CKLink.
    """
    
    DLL_PATH = os.path.dirname(__file__)
    WORK_PATH = os.getcwd()

    def open_required(func):
        def wrapper(self, *args, **kwargs):
            if not self.tgt:
                raise errors.CKLinkException('Error: Target is not open')
            return func(self, *args, **kwargs)
        return wrapper
    
    def change_working_path(func):
        def wrapper(self, *args, **kwargs):
            os.chdir(CKLink.DLL_PATH)
            func(self, *args, **kwargs)
            os.chdir(CKLink.WORK_PATH)
        return wrapper

    def __init__(self, **kwargs):
        self.tgt = None
        self.cfg = structs.DebuggerDerverCfg()
        if "dlldir" in kwargs:
            CKLink.DLL_PATH = kwargs["dlldir"]
        else:
            CKLink.DLL_PATH = os.path.dirname(__file__)
        self.initialize(**kwargs)
    
    @change_working_path
    def initialize(self, **kwargs):
        self.find_library()
        self.dll_utils.init_default_config(ctypes.byref(self.cfg))
        self.cfg.root_path = CKLink.DLL_PATH.encode('gbk')
        if "vid" in kwargs:
            self.cfg.link.vid = kwargs["vid"]
        if "pid" in kwargs:
            self.cfg.link.pid = kwargs["pid"]
        if "sn" in kwargs:
            self.cfg.link.serial = kwargs["sn"].encode('gbk')           
        if "arch" in kwargs:
            self.cfg.arch.debug_arch = kwargs["arch"]  # 0:none, 1:csky, 2:riscv, 3:auto
        self.cfg.arch.no_cache_flush = 1  # 执行单步和退出调试模式时不刷cache
        self.dll_utils.dbg_debug_channel_init(self.cfg.misc.msgout, self.cfg.misc.errout, self.cfg.misc.verbose)
        self.dll_target.target_init.argtypes = [ctypes.POINTER(structs.DebuggerDerverCfg)]
        self.dll_target.target_init(ctypes.byref(self.cfg))
           
    def find_library(self):
        if sys.platform == 'win32':
            python_version = struct.calcsize("P") * 8
            if python_version == 32:
                self.dll_target = ctypes.cdll.LoadLibrary('Target.dll')
                self.dll_utils = ctypes.cdll.LoadLibrary('Utils.dll')
            else:
                raise errors.CKLinkException('Error: Python must be 32-bit version')
        elif sys.platform.startswith('linux'):
            self.dll_stdc = ctypes.CDLL("libstdc++.so.6", mode=ctypes.RTLD_GLOBAL)        
            self.dll_usb = ctypes.CDLL("./libusb-1.0.so", mode=ctypes.RTLD_GLOBAL)
            self.dll_utils = ctypes.CDLL("libUtils.so", mode=ctypes.RTLD_GLOBAL)
            self.dll_cklink = ctypes.CDLL("links/CK-Link/libCklink.so", mode=ctypes.RTLD_GLOBAL)
            self.dll_scripts = ctypes.CDLL("libScripts.so", mode=ctypes.RTLD_GLOBAL)
            self.dll_xml = ctypes.CDLL("libXml.so", mode=ctypes.RTLD_GLOBAL)
            self.dll_target = ctypes.CDLL("libTarget.so")
            
            self.dll_stdc.malloc.restype = ctypes.c_void_p
            self.dll_stdc.malloc.argtypes = [ctypes.c_size_t]
            self.dll_stdc.free.argtypes = [ctypes.c_void_p]
            self.mem1 = self.dll_stdc.malloc(1024000)
            self.dll_usb.malloc.restype = ctypes.c_void_p
            self.dll_usb.malloc.argtypes = [ctypes.c_size_t]
            self.dll_usb.free.argtypes = [ctypes.c_void_p]
            self.mem2 = self.dll_usb.malloc(1024000)
            self.dll_utils.malloc.restype = ctypes.c_void_p
            self.dll_utils.malloc.argtypes = [ctypes.c_size_t]
            self.dll_utils.free.argtypes = [ctypes.c_void_p]
            self.mem3 = self.dll_utils.malloc(1024000)
            self.dll_cklink.malloc.restype = ctypes.c_void_p
            self.dll_cklink.malloc.argtypes = [ctypes.c_size_t]
            self.dll_cklink.free.argtypes = [ctypes.c_void_p]
            self.mem4 = self.dll_cklink.malloc(1024000)
            self.dll_scripts.malloc.restype = ctypes.c_void_p
            self.dll_scripts.malloc.argtypes = [ctypes.c_size_t]
            self.dll_scripts.free.argtypes = [ctypes.c_void_p]
            self.mem5 = self.dll_scripts.malloc(1024000)
            self.dll_xml.malloc.restype = ctypes.c_void_p
            self.dll_xml.malloc.argtypes = [ctypes.c_size_t]
            self.dll_xml.free.argtypes = [ctypes.c_void_p]
            self.mem6 = self.dll_xml.malloc(1024000)
            self.dll_target.malloc.restype = ctypes.c_void_p
            self.dll_target.malloc.argtypes = [ctypes.c_size_t]
            self.dll_target.free.argtypes = [ctypes.c_void_p]        
            self.ptr1 = ctypes.cast(self.dll_target.malloc(1024000), ctypes.POINTER(structs.Target))
            self.ptr2 = ctypes.cast(self.dll_target.malloc(1024000), ctypes.POINTER(structs.Register))
            self.ptr3 = ctypes.cast(self.dll_target.malloc(1024000), ctypes.POINTER(structs.DebuggerDerverCfg))
                    
    def print_version(self):
        fn_type_output = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p)
        self.output = fn_type_output(output_func)
        self.dll_target.target_print_version(self.output)
    
    def connected(self):
        """Returns whether a CKLink is connected.

        Args:
          self (CKLink): the ``CKLink`` instance

        Returns:
          ``True`` if the CKLink is open and connected, otherwise ``False``.
        """
        if self.tgt:
            res = self.dll_target.target_is_connected(self.tgt)
            return True if res else False
        else: 
            return False

    def open(self):
        self.dll_target.target_open.argtypes = [ctypes.POINTER(structs.DebuggerDerverCfg)]
        self.dll_target.target_open.restype = ctypes.POINTER(structs.Target)
        self.tgt = self.dll_target.target_open(ctypes.byref(self.cfg))
        self.cfg.target = self.tgt.contents
        # print("handle is " + str(self.tgt))
        # return a handle(an address comes from malloc)
        if not self.tgt:
            raise errors.CKLinkException('Error: Open target failed')
    
    def close(self):
        if self.tgt:
            self.dll_target.target_close.argtypes = [ctypes.POINTER(structs.Target)]
            res = self.dll_target.target_close(self.tgt)
            if self.dll_target:
                if sys.platform == 'win32':
                    _ctypes.FreeLibrary(self.dll_target._handle)
                elif sys.platform.startswith('linux'):
                
                    handle1 = self.dll_target._handle
                    handle2 = self.dll_stdc._handle
                    handle3 = self.dll_usb._handle
                    handle4 = self.dll_utils._handle
                    handle5 = self.dll_cklink._handle
                    handle6 = self.dll_scripts._handle
                    handle7 = self.dll_xml._handle
                    
                    _ctypes.dlclose(handle1)
                    _ctypes.dlclose(handle2)
                    _ctypes.dlclose(handle3)
                    _ctypes.dlclose(handle4)
                    _ctypes.dlclose(handle5)
                    _ctypes.dlclose(handle6)
                    _ctypes.dlclose(handle7)
                       
                    print("free memory")
                    self.dll_target.free(self.ptr1)
                    self.dll_target.free(self.ptr2)
                    self.dll_target.free(self.ptr3)
                    self.dll_stdc.free(self.mem1) 
                    self.dll_usb.free(self.mem2)
                    self.dll_utils.free(self.mem3)
                    self.dll_cklink.free(self.mem4)
                    self.dll_scripts.free(self.mem5)
                    self.dll_xml.free(self.mem6)
                    
                    del self.dll_stdc
                    del self.dll_usb
                    del self.dll_utils
                    del self.dll_cklink
                    del self.dll_scripts
                    del self.dll_xml
                    del self.dll_target

            if not res:
                self.tgt = None
                return True
            else:
                return False 
  
    @open_required
    def halt(self):
        """Halt the target
        
        Args:
          self (CKLink): the ``CKLink`` instance

        Returns:
          ``True`` if halted, ``False`` otherwise.
        """
        self.dll_target.target_halt.argtypes = [ctypes.POINTER(structs.Target)]
        res = self.dll_target.target_halt(self.tgt)
        return True if not res else False
    
    @open_required
    def reset(self, type=1):
        """Reset the target
        
        Args:
          self (CKLink): the ``CKLink`` instance
          type (int): 2, nreset, 1 hard, 0, software

        Returns:
          ``True`` if success, ``False`` otherwise.
        """
        self.dll_target.target_reset.argtypes = [ctypes.POINTER(structs.Target), ctypes.c_uint]
        res = self.dll_target.target_reset(self.tgt, type)
        return True if not res else False
    
    @open_required
    def resume(self):
        self.dll_target.target_resume.argtypes = [ctypes.POINTER(structs.Target)]
        res = self.dll_target.target_resume(self.tgt)
        return True if not res else False
      
    @open_required
    def write_memory(self, addr, data):
        """Write memory to target

        Args:
          self (CKLink): the ``CKLink`` instance
          addr (int): start address to write to
          data (bytes): data to write

        Returns:
          ``True`` if success, ``False`` otherwise
        """
        addr = ctypes.c_uint64(addr)
        size = len(data)
        wbuff = (ctypes.c_char*size)(*(data))
        self.dll_target.target_write_memory.argtypes = [ctypes.POINTER(structs.Target), ctypes.c_uint64, ctypes.c_char_p]
        res = self.dll_target.target_write_memory(self.tgt, addr, wbuff, size)
        return True if not res else False 
    
    @open_required
    def read_memory(self, addr, size):
        """Read memory from target

        Args:
          self (CKLink): the ``CKLink`` instance
          addr (int): start address to read from
          size (int): size to read

        Returns:
          data (bytes) read from memory
        """
        addr = ctypes.c_uint64(addr)
        rbuff = (ctypes.c_char*size)()
        self.dll_target.target_read_memory.argtypes = [ctypes.POINTER(structs.Target), ctypes.c_uint64, ctypes.c_char_p, ctypes.c_uint]
        res = self.dll_target.target_read_memory(self.tgt, addr, rbuff, size)
        if not res:
            return rbuff[:]
        else:
            raise errors.CKLinkException('Error: Read memory failed')
    
    @open_required
    def write_cpu_reg(self, reg_index, value):
        """Write cpu register
        
        Args:
          self (CKLink): the ``CKLink`` instance
          reg_index (int): reigster to be written
          value (int): the value to write to the register
          
        Returns:
          ``True`` if success, ``False`` otherwise
        """
        rn = structs.Register()
        rn.num = reg_index
        rn.value.val32 = value
        self.dll_target.target_write_cpu_reg.argtypes = [ctypes.POINTER(structs.Target), ctypes.POINTER(structs.Register)]
        res = self.dll_target.target_write_cpu_reg(self.tgt, ctypes.byref(rn))
        return True if not res else False
    
    @open_required
    def read_cpu_reg(self, reg_index):
        """Read cpu register
       
        Args:
          self (CKLink): the ``CKLink`` instance
          reg_index (int): reigster to read from
          
        Returns:
          The value (int) stored in the given register
        """
        rn = structs.Register()
        rn.num = reg_index
        res = self.dll_target.target_read_cpu_reg(self.tgt, ctypes.byref(rn))
        if not res:
            return rn.value.val32
        else:
            raise errors.CKLinkException('Read cpu register failed')
    
    @open_required
    def add_soft_breakpoint(self, addr, length=2):
        """Sets a soft breakpoint at the specified address

        Args:
          self (CKLink): the ``CKLink`` instance
          addr (int): the address where the breakpoint will be set
          length (int): the breakpoint length, it could be 2 or 4

        Returns:
          ``True`` if success, ``False`` otherwise
        """
        res = self.dll_target.breakpoint_add(self.tgt, addr, length, 0)
        return True if not res else False
    
    @open_required
    def add_hard_breakpoint(self, addr, length=2):
        """Sets a hard breakpoint at the specified address

        Args:
          self (CKLink): the ``CKLink`` instance
          addr (int): the address where the breakpoint will be set
          length (int): the breakpoint length, it could be 2 or 4

        Returns:
          ``True`` if success, ``False`` otherwise
        """
        res = self.dll_target.breakpoint_add(self.tgt, addr, length, 1)
        return True if not res else False
    
    @open_required          
    def clear_breakpoint(self):
        res = self.dll_target.breakpoint_clear(self.tgt)
        return True if not res else False
    
    @open_required          
    def enable_ddc(self):
        res = self.dll_target.target_enable_ddc(self.tgt, 1)
        return True if not res else False 
    
    @open_required
    def disable_ddc(self):
        res = self.dll_target.target_enable_ddc(self.tgt, 0)
        return True if not res else False
    
    @open_required
    def single_step(self):
        res = self.dll_target.target_single_step(self.tgt)
        return True if not res else False
    
    @open_required
    def enable_cache_flush(self):
        res = self.dll_target.target_enable_cache_flush(self.tgt, 1)
        return True if not res else False
    
    @open_required
    def disable_cache_flush(self):
        res = self.dll_target.target_enable_cache_flush(self.tgt, 0)
        return True if not res else False

    











