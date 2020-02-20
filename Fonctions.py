#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:08:58 2020

@author: HOAREAU.LyseMay
"""

#Constants

theta1 = 4200
theta2 = 0.11
theta3 = 37
gamma = 0.35
S_F = 0.74
rho_G_1 = 0.06
rho_G_2 = -0.027
rho_B_1 = 0.023
rho_B_2 = -0.02
phi1 = 283
phi2 = 8.6
Rs = 2.90
a1 = 0.79
a2 = 0.01

#Fonctions 



class Household:
    
    def Wages(self, GDP):
        return (1-gamma)*GDP
    
    def Housing_Transaction(self, Delta_Ph):
        return phi1 + phi2*(Delta_Ph)
    
class Government:
    
    def Government_Bond_Price(self, B_G_ICPF, B_G_ROW,B_G_CB, b_G):
        return (B_G_ICPF + B_G_ROW + B_G_CB)/b_G
    
    def NetLending_G(self, Tx_H, Tx_F, G, T_H, T_F, i_BG, B_G_ICPF, B_G_ROW):
        return Tx_H + Tx_F - G - T_H - T_F - i_BG*(B_G_ICPF + B_G_ROW)
    
class Bank:
    
    def Bank_Bond_Price(self, B_B_ICPF, B_B_ROW, b_B):
        return (B_B_ICPF + B_B_ROW) / b_B
    
    def Interest_rate_BB(self, i_BG):
        return rho_B_1 + i_BG + rho_B_2 * Bank.Bank_Bond_Price(self,B_B_ICPF, B_B_ROW, b_B)
    