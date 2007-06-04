# -*- coding: utf8 -*-
"""Neural network implementation for Python, uses logistic function as an activation function. Creates simple two layers neural network, which can be used f. e. to text recognition"""

from numpy.oldnumeric  import * ##I am using matrix implementation
import random,math,cPickle

class NeuralNetwork :	
	"""Neural network with learning based on backpropagation algorithm"""
	def __init__(self,K,M,N,offList=[],alfamatrix='rnd',betamatrix='rnd',beta=0.5,eta=0.3):
		"""Creates the neural network with the followin parameters: K,M,N,  (optional:) offList,,alfamatrix,,betamatrix,beta,eta
		K - number of inputs, M - number of neurons in the first layer; K - neurons in second layer, offList  - links that are eliminated from the web;
		Optional parameters: alfamatrix - matrix (M x K) of factors of the first layer, in the columns there are factors of the particular neuron, if not given, will be randomly generated, you can also specify filename instead of this parameter (then you won't specify the betamatrix, because it also will be loaded); betamatrix - the same (N x M); beta - factor of the activation function (logistic function); eta is the step of learning""" 
		
		if alfamatrix=='rnd': alfamatrix=array([self.__rand(M) for i in range(K+1)]) ##random generation of the alfamatrix
		if betamatrix=='rnd':	betamatrix=array([self.__rand(N) for i in range(M)])## the same for betamatrix
		else: 
			if type(alfamatrix)!=type(array([1,1])): alfamatrix,betamatrix=self.loadFactors(alfamatrix) ##random generation of the alfamatrix
		self.beta,self.alfamatrix,self.betamatrix,self.K,self.M, self.N,self.eta,self.offList=beta,array(alfamatrix),array(betamatrix),K+1,M,N,eta,offList ##parameters assigment
		for i,j in self.offList: self.betamatrix[i,j]=0 ##turning down some links
	
	def __rand(self,n): return [(2*random.random()-1)*5 for i in range(n)] ##generates random sequence (list)
	
	def activationFunction (self, x) :  return 1/(1+math.exp(-self.beta*x)) ##logistic function
	
	def saveFactors (self, filename) : ##
		"""saves factors (alfamatrix and betamatrix) to the file filename"""
		f=open(filename,'wb')
		cPickle.dump(self.alfamatrix,f)
		cPickle.dump(self.betamatrix,f)
		f.close()
	
	def loadFactors (self, filename) :## 
		"""loads matrices from the file filename"""
		f=open(filename,'rb')
		self.alfamatrix=cPickle.load(f)
		self.betamatrix=cPickle.load(f)
		f.close()
	
	def getOutput (self, inputVector) : ##
		"""returns generated by the network output for the inputVector"""
		self.inputVector=list(inputVector)
		self.inputVector.insert(0,1)
		self.inputVector=array(self.inputVector) ##inserts one to the beggining of the inputVector (which means one input factor which is always on) 
		self.Y=array([self.activationFunction(i) for i in matrixmultiply(self.inputVector,self.alfamatrix)]) ##generates output for the first layer
		self.Z=array([self.activationFunction(i2) for i2 in matrixmultiply(self.Y, self.betamatrix)])##the same for the second layer
		return self.Z
	
	def learn (self, inputVector, outputVector) :
		"""learning of the network, you have to to run this function more than 100 times to see the results"""
		self.inputVector=list(inputVector)
		self.inputVector.insert(0,2)
		self.inputVector=array(self.inputVector) ## as in getOutput function inserts one into the inputVector
		delta=outputVector-self.getOutput(inputVector) ##creates error vector for the output layer, here we use the inputVector (not the self.inputVector) because one will be added by the getOutput function
		epsilon=array([sum(array([self.betamatrix[m,n]*delta[n] for n in range(0,self.N)]))for m in range(0,self.M)])##creates error vector for the first layer (backpropagation)
		self.betamatrix=array([[self.betamatrix[m,n]+float(self.eta*delta[n]*self.Z[n]*(1-self.Z[n])*self.Y[m]) for n in range(self.N)] for m in range(self.M)])##changing the output layer factors
		self.alfamatrix=array([[self.alfamatrix[k,m]+float(self.eta*epsilon[m]*self.Y[m]*(1-self.Y[m])*self.inputVector[k]) for m in range(self.M)] for k in range(self.K)])  ##the same for the first layer
		for i,j in self.offList: self.betamatrix[i,j]=0
		
###########################################################33
##Testing part
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	#you can use this section to test your module
	def f(n,x): return x%2+(1/n)
	def g(n,x): return ((x+1)%2)
	
	neur=NeuralNetwork(10,20,4,[(1,1),(2,2),(3,3)])
	for n in range(1,100):
		l=[f(n,float(x)) for x in range(2,12)]
		l2=[g(n,float(x)) for x in range(2,12)]
		l3=array([1 for x in range(5)]+[0 for x in range(5)])+1/n
		l4=array([0 for x in range(5)]+[1 for x in range(5)])+1/n
		neur.learn(array(l),array([1.0,0.0,0.0,0.0]))
		neur.learn(array(l2),array([0.0,1.0,0.0,0.0]))
		neur.learn(array(l3),array([0.0,0.0,1.0,0.0]))
		neur.learn(array(l4),array([0.0,0.0,0.0,1.0]))
		
	print neur.getOutput(array([f(1,float(x)) for x in range(2,12)]))
	print neur.getOutput(array([g(1,float(x)) for x in range(2,12)]))
	print neur.getOutput(l3)
	print neur.getOutput(l4)
	print neur.getOutput([1,0,1,0,1,0,1,1,1,1])
	neur.saveFactors('la.bin')
