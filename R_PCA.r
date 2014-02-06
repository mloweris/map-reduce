#Example file for working with genotype data
require(ggplot2)

#this will have to change to the correct directory
setwd("/Users/uqmkel13/Documents/Projects/Brazil Course/Course2/Workshop/datafiles")

genotypes<-read.csv('genotypes1000.txt')
M<-as.matrix(genotypes[,2:ncol(genotypes)])


# Need to convert the genotypes to a GRM 
#this could also be done faster if there were Matrix operations 
nanimals<-nrow(M)
nmarkers=ncol(M)
p<-as.matrix(apply(M,2,mean))/2.

# Yang 
p2=matrix(rep(p,nanimals),nrow=nanimals,ncol=nmarkers,byrow=T )
Z = M  -p2
G = (Z%*%t(Z) )/ nmarkers #SPEED UP HERE



#PCA that needs to be applied
princomOut<-princomp(G)  #SPEED UP HERE
plot(princomOut$loadings)
