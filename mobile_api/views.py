from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
import requests
from rest_framework.response import Response
from rest_framework import status
import json
import traceback

from rest_framework.views import APIView
class GenerateAddressViewset(viewsets.ViewSet):
    def create(self,request):
        try:
            url = 'https://api.cryptoapis.io/v1/bc/btc/mainnet/address'
            headers = {
            "Content-Type": "application/json",
            "X-API-Key": "9bbaea5ee68777d437f1049ca78db6fedd8d7e3e"
            }
            response = requests.post(url, headers=headers, data={})
            data = json.loads(response.text)
            return Response({'response': data,"success":True},status=status.HTTP_200_OK)

        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK) 

class GetDetailByAddressViewset(viewsets.ViewSet):
    def retrieve(self,request,pk=None):
        try:
            if not pk:
                raise Exception("please enter address id")
            if pk:
                url = 'https://api.cryptoapis.io/v1/bc/btc/mainnet/address/' + pk
                headers = {
                    "Content-Type": "application/json",
                    "X-API-Key": "9bbaea5ee68777d437f1049ca78db6fedd8d7e3e"
                }
                response = requests.get(url, headers=headers)
                data = json.loads(response.text)
                return Response({'response': data,"success":True},status=status.HTTP_200_OK)

        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK) 


class GetTransactionByAddressViewset(viewsets.ViewSet):
    def retrieve(self,request,pk=None):
        try:
            if not pk:
                raise Exception("please enter address id")
            if pk:
                url = 'https://api.cryptoapis.io/v1/bc/btc/testnet/txs/basic/txid/' + pk
                headers = {
                    "Content-Type": "application/json",
                    "X-API-Key": "9bbaea5ee68777d437f1049ca78db6fedd8d7e3e"
                }
                response = requests.get(url, headers=headers)
                data = json.loads(response.text)

                return Response({'response': data,"success":True},status=status.HTTP_200_OK)

        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK) 

class GetTransactionFeeViewset(viewsets.ViewSet):
    def list(self,request):
        try:
            
            url = 'https://api.cryptoapis.io/v1/exchanges/'
            headers = {
                "Content-Type": "application/json",
                "X-API-Key": "9bbaea5ee68777d437f1049ca78db6fedd8d7e3e"
            }
            response = requests.get(url, headers=headers)
            data = json.loads(response.text)

            return Response({'response': data,"success":True},status=status.HTTP_200_OK)

        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK) 

# class ListWalletPriceViewset(viewsets.ViewSet):
#     def list(self,request):
#         try:
#             print(request.GET)
#             walletname = request.GET.get('walletname')
#             address_count = request.GET.get('address_count')
#             password = request.GET.get('password')
#             url = 'https://api.cryptoapis.io/v1/exchange-rates/'+request.GET.get('base_id')+'/'+request.GET.get('quote_id')
#             headers = {
#             "Content-Type": "application/json",
#             "X-API-Key": "9bbaea5ee68777d437f1049ca78db6fedd8d7e3e"
#             }
#             response = requests.get(url, headers=headers)
#             data = json.loads(response.text)

#             return Response({'response': data,"success":True},status=status.HTTP_200_OK)

#         except Exception as error:
#             traceback.print_exc()
#             return Response({"message":str(error),"success":False},status=status.HTTP_200_OK) 


class ExPrice(APIView):
    def get(self, request):
        base_id = request.GET.get('base_id')
        quote_id = request.GET.get('quote_id')
        url = 'https://api.cryptoapis.io/v1/exchange-rates/'+base_id+'/'+quote_id
        headers = {
        "Content-Type": "application/json",
        "X-API-Key": "9bbaea5ee68777d437f1049ca78db6fedd8d7e3e"
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)

        return Response({'response': data,"success":True},status=status.HTTP_200_OK)
