#!/usr/bin/env python2
# coding: UTF-8

from unicorn import *
from unicorn.x86_const import *
import sys

# memory address where emulation starts
ADDRESS = 0x1000000

# initialize unicorn emulator
mu = Uc(UC_ARCH_X86, UC_MODE_32)
# map 4MB for this emulation
mu.mem_map(ADDRESS, 4 * 1024 * 1024)

binary = ''
if len(sys.argv) == 2:
    with open(sys.argv[1], 'rb') as f:
        binary = f.read()
else:
    binary = b"\x41\x4a" # INC ecx; DEC edx


mu.mem_write(ADDRESS, binary)

# emulate code in infinite time & unlimited instructions
mu.emu_start(ADDRESS, ADDRESS + len(binary))

r_eax = mu.reg_read(UC_X86_REG_EAX)
r_ebx = mu.reg_read(UC_X86_REG_EBX)
r_ecx = mu.reg_read(UC_X86_REG_ECX)
r_edx = mu.reg_read(UC_X86_REG_EDX)
r_ebp = mu.reg_read(UC_X86_REG_EBP)
r_esp = mu.reg_read(UC_X86_REG_ESP)
r_edi = mu.reg_read(UC_X86_REG_EDI)
r_esi = mu.reg_read(UC_X86_REG_ESI)
r_eip = mu.reg_read(UC_X86_REG_EIP)
r_eflags = mu.reg_read(UC_X86_REG_EFLAGS)

print(">>> EAX = 0x%x" % r_eax)
print(">>> EBX = 0x%x" % r_ebx)
print(">>> ECX = 0x%x" % r_ecx)
print(">>> EDX = 0x%x" % r_edx)
print(">>> EBP = 0x%x" % r_ebp)
print(">>> ESP = 0x%x" % r_esp)
print(">>> EDI = 0x%x" % r_edi)
print(">>> ESI = 0x%x" % r_esi)
print(">>> EIP = 0x%x" % r_eip)
print(">>> EFLAGS = 0x%x" % r_eflags)