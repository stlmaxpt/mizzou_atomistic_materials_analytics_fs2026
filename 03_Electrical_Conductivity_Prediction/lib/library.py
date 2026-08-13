# Written by Marcus Schwarting in collaboration with the National Renewable
# Energy Laboratories. For further information please see the website 
# https://htem.nrel.gov/ as well as the recent publication on this work,
# [insert reference to upcoming paper here]. The goal of this project is to
# further the objectives laid out in the strategic objectives for the
# Materials Genome Initiative.
# 
# For further information on this code project, please email:
# Marcus Schwarting ==> marcus.schwarting@nrel.gov

#API SAMPLE(S) SPECIFIC!

import urllib, json
import pandas as pd
from urllib.error import HTTPError

class Library:
    def __init__(self,identity):
        self.identity = identity

    @staticmethod
    def search_by_ids(ids_list):
        obj_list = []
        for i in ids_list:
            obj_list.append(Library(i))
        return obj_list

    @staticmethod
    def search_by_composition(only=[],not_including=[],any_of=[]):
        elt_url = 'https://htem-api.nrel.gov/api/sample_library?element='
        for i in only:
            if i == only[-1]:
                elt_url = elt_url+str(i)
            else:
                elt_url = elt_url+str(i)+','
        #print(elt_url)
        with urllib.request.urlopen(elt_url) as response:
            data = json.load(response)
            #print(data)
        ids_list = []
        
        #print(json.loads(response.read()))
        for i in data:
            elts = str(i['elements'])
            violated = False
            for k in not_including:
                if k in elts:
                    violated = True
            l = 0
            for k in only:
                if k in elts:
                    l = l+1
            #print('L is ' + str(l))
            #print('Only is ' + str(len(only)))
            if l == len(only) and violated == False:
                ids_list.append(i['id'])
                #print(violated)
            else:
                pass
        obj_list = []
        #print(ids_list)
        for i in ids_list:
            obj_list.append(Library(i))
        return obj_list

            
    def properties(self):
        url = 'https://htem-api.nrel.gov/api/sample_library/'+str(self.identity)
        df = pd.DataFrame()
        try:
            with urllib.request.urlopen(url) as response:
                data = json.load(response)
            #response = urllib.request.urlopen(url)
            #data = json.loads(response.read())
        
            for i in data:
                df[i] = [data[i]]
        except:
            pass
        return df

    def spectra(self,which):
        url = 'https://htem-api.nrel.gov/api/sample_library/'+str(self)
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
        positions = data['sample_ids']
        df = pd.DataFrame()

        for k in positions:
            try:
                url = 'https://htem-api.nrel.gov/api/sample/'+str(k)
                with urllib.request.urlopen(url) as response:
                    data = json.load(response)
                leveled_position = data['position']
                if which == 'xrf':
                    try:
                        #b = len(df)
                        #for i in range(len(data['xrf_compounds'])):
                        #    df.at[b,'xrf_concentrations_'+(data['xrf_compounds'][i])] = data['xrf_concentration'][i]     
                        df['xrf_compounds_'+str(leveled_position)] = data['xrf_compounds']
                        df['xrf_concentrations_'+str(leveled_position)] = data['xrf_concentration']
                    except:
                        #display('No xrf data')
                        pass
                elif which == 'xrd': 
                    try:
                        df['xrd_angle_'+str(leveled_position)] = data['xrd_angle']
                        df['xrd_background_'+str(leveled_position)] = data['xrd_background']
                        df['xrd_intensity_'+str(leveled_position)] = data['xrd_intensity']
                    except:
                        #display('No xrd data')
                        pass
                elif which == 'opt':
                    info_df = pd.DataFrame()
                    extra_df = pd.DataFrame()
                    try:
                        info_df['peak_count_'+str(leveled_position)] = list([data['peak_count']])
                        info_df['opt_average_vis_trans_'+str(leveled_position)] = list([data['opt_average_vis_trans']])
                        info_df['opt_direct_bandgap_'+str(leveled_position)] = list([data['opt_direct_bandgap']])
                        
                        extra_df['xyz_mm_'+str(leveled_position)] = data['xyz_mm']
                    except:
                        pass
                    uvir_df = pd.DataFrame()
                    try:
                        uvir_df['opt_uvir_wavelength_'+str(leveled_position)] = data['opt_uvir_wavelength']
                        uvir_df['opt_uvir_response_'+str(leveled_position)] = data['opt_uvir_response']
                    except KeyError: #No uvir available
                        pass
                    uvit_df = pd.DataFrame()
                    try:
                        uvit_df['opt_uvit_wave_'+str(leveled_position)] = data['opt_uvit_wavelength']
                        uvit_df['opt_uvit_response_'+str(leveled_position)] = data['opt_uvit_response']
                    except KeyError: #No uvit available
                        pass
                    nirr_df = pd.DataFrame()
                    try:
                        nirr_df['opt_nirr_wavelength_'+str(leveled_position)] = data['opt_nirr_wavelength']
                        nirr_df['opt_nirr_response_'+str(leveled_position)] = data['opt_nirr_response']
                    except KeyError: #No nirr available
                        pass
                    nirt_df = pd.DataFrame()
                    try:
                        nirt_df['opt_nirt_wavelength_'+str(leveled_position)] = data['opt_nirt_wavelength']
                        nirt_df['opt_nirt_response_'+str(leveled_position)] = data['opt_nirt_response']
                    except KeyError: #No nirt available
                        pass
                    opt_df = pd.DataFrame()
                    try:
                        opt_df['opt_energy_'+str(leveled_position)] = data['opt_energy']
                        opt_df['opt_wavelength_'+str(leveled_position)] = data['opt_wavelength']
                        opt_df['opt_normalized_transmittance_'+str(leveled_position)] = data['opt_normalized_transmittance']
                        opt_df['opt_absorption_coefficient_'+str(leveled_position)] = data['opt_absorption_coefficient']
                    except: #No opt available
                        #display('No optical data')
                        pass
                    pos_df = pd.concat([info_df,extra_df,uvir_df,uvit_df,nirr_df,nirt_df,opt_df],axis=1) 
                    df = pd.concat([df,pos_df],axis=1)
                elif which == 'ele':
                    ele_df = pd.DataFrame()
                    info_df = pd.DataFrame()
                    try:
                        ele_df['fpm_voltage_volts_'+str(leveled_position)] = data['fpm_voltage_volts'] #5
                        ele_df['fpm_current_amps_'+str(leveled_position)] = data['fpm_current_amps'] #5
                        
                        info_df['fpm_sheet_resistance_'+str(leveled_position)] = list([data['fpm_sheet_resistance']]) #1 
                        info_df['fpm_standard_deviation_'+str(leveled_position)] = list([data['fpm_standard_deviation']]) #1
                        info_df['fpm_resistivity_'+str(leveled_position)] = list([data['fpm_resistivity']]) #1
                        info_df['fpm_conductivity_'+str(leveled_position)] = list([data['fpm_conductivity']]) #1
                        info_df['absolute_temp_c_'+str(leveled_position)] = list([data['absolute_temp_c']]) 
                        #if data['STRING'] == int else 
                    except:
                        #display('No electrical data')
                        pass
                    pos_df = pd.concat([ele_df,info_df],axis=1)
                    df = pd.concat([df,pos_df],axis=1)
                else:
                    df = pd.DataFrame()
            except HTTPError as err: #Data missing. Moving on.
                if err.code == 400:
                    print('Sample not found')
                    continue
        if df.empty:
            print('No data')
        return df
        