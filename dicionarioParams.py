dParams = {}

#keys = ['UF','PROCESSO','RENOVACAO','PRIORIDADE1','PRIORIDADE2','ECONOMIA','COSTUME','REF_CARGO']

dParams['UF'] = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
dParams['PROCESSO'] = [str(i) for i in range(1,4)]
dParams['RENOVACAO'] = [str(i) for i in range(1,4)]
dParams['PRIORIDADE1'] = [str(i) for i in range(1,6)]
dParams['PRIORIDADE2'] = [str(i) for i in range(6,25)]
dParams['ECONOMIA'] = [str(i) for i in range(1,4)]
dParams['COSTUME'] = [str(i) for i in range(1,3)]
dParams['REF_CARGO'] = [str(i) for i in range(1,4)]

with open('parametros.dat','w') as saida:
	saida.write('UF\tPROCESSO\tRENOVACAO\tPRIORIDADE1\tPRIORIDADE2\tECONOMIA\tCOSTUME\tREF_CARGO\n')
	for uf in dParams['UF']:
		for processo in dParams['PROCESSO']:
			for renovacao in dParams['RENOVACAO']:
				for prioridade1 in dParams['PRIORIDADE1']:
					for prioridade2 in dParams['PRIORIDADE2']:
						for economia in dParams['ECONOMIA']:
							for costume in dParams['COSTUME']:
								for ref_cargo in dParams['REF_CARGO']:
									saida.write(uf+'\t'+processo+'\t'+renovacao+'\t'+prioridade1+'\t'+prioridade2+'\t'+economia+'\t'+costume+'\t'+ref_cargo+'\n')
