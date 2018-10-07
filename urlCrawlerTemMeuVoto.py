import urllib.request, json, sys

with open('parametros.dat','r') as parametros:
	header = parametros.readline()	
	for line in parametros:

		lParams = line.rstrip().split('\t')
		UF = lParams[0]
		url = "https://temmeuvoto.com/api/listCandidatos/?uf="+lParams[0]+"&processo="+lParams[1]+"&renovacao="+lParams[2]+"&prioridade1="+lParams[3]+"&prioridade2="+lParams[4]+"&economia="+lParams[5]+"&costume="+lParams[6]+"&ref_cargo="+lParams[7]+"&page="
		
		print('UF ',UF,' realizando a chamada')
		for i in range(0,500):			

			with urllib.request.urlopen(url.replace("page=","page="+str(i))) as urlOpened:
				data = json.loads(urlOpened.read().decode())
			
			listaCandidatos =  data['data']['list']		

			if(not listaCandidatos):
				print(str('UF: '+lParams[0]),i,' páginas encontradas!')
				break
			else:
				with open(lParams[0]+'/'+lParams[0]+'_'+lParams[1]+'_'+lParams[2]+'_'+lParams[3]+'_'+lParams[4]+'_'+lParams[5]+'_'+lParams[6]+'_'+lParams[7]+'_'+'.dat','a') as saida:
					for e in listaCandidatos:
						saida.write(str(e)+ '\n')
	