#!/usr/bin/Rscript

##sample ID : `ls -hl /readonly/Share2/home/lulab/jinyunfan/exSeek-dev/output/PBMC/bam`
##most important columns/headers: CDR3aa	V	frequency	(Group)

#print(dim,quote=FALSE,file=stdout())
#source(file = "/BioII/lulab_b/baopengfei/2020proj/TCR/lulab_pbmc/scripts/filter.R", /BioII/lulab_b/baopengfei/2020proj/TCR/lulab_pbmc/TRUST4-output/fq-output 2 CRC-2415350)

args = commandArgs(trailingOnly=TRUE)
if (length(args)!=3) {
 stop("usage: Rscript filter.R indir outdir sampleid")
} else if (length(args)==3) {
 print(paste("indir:",args[1],";outdir:",args[2],",sampleid:",args[3]))
 print(paste("start",args[3],"filter at",Sys.time()))
}

# read input
input.name <- paste(args[1],"/",args[3],"/",args[3],"_report.tsv",sep = "")
trust4.fq <- read.delim2(file = input.name)
trust4.fq <- trust4.fq[,c(4,5,2)]
dim0 <- dim(trust4.fq)
print(dim0)

# remove/filter poor/low quality CDR3 sequences/calls/records
## 1.rm record gene locus was not solved
trust4.fq$V.nchar <- nchar(as.vector(trust4.fq$V))
trust4.fq <- trust4.fq[trust4.fq$V.nchar > 1,] 
dim1 <- dim(trust4.fq)
print(dim1)

## 2.rm record's sequence length was <10 or >24
trust4.fq$aa.length <- nchar(as.vector(trust4.fq$CDR3aa))
trust4.fq <- trust4.fq[trust4.fq$aa.length >= 10 & trust4.fq$aa.length <= 24, ] 
dim2 <- dim(trust4.fq)
print(dim2)

###optional: length distribution plot
###frequency.seq <- table(trust4.fq$aa.length)
###frequency.seq
###plot(frequency.seq)

## 3.rm record's CDR3.aa has special symbol: _ * . + X ?        NOTE:perl = F
sequence_without_special <- trust4.fq$CDR3aa %in% grep("[^A-Z]", trust4.fq$CDR3aa, value = TRUE, ignore.case = T, invert = T)
trust4.fq <- subset(x = trust4.fq, subset = sequence_without_special)
dim3 <- dim(trust4.fq)
print(dim3)

## 4.rm record's CDR3.aa not start with C, end with F
###filter.head <- grep(pattern="^C", x = trust4.fq$CDR3aa, fixed = F,ignore.case = T, value = T)
###filter.head
###length(filter.head)
filter.head <- grep(pattern="^C", x = trust4.fq$CDR3aa, fixed = F,ignore.case = T)
trust4.fq <- trust4.fq[filter.head, ]

###filter.tail
###filter.tail <- grep(pattern="F$", x = trust4.fq$CDR3aa, fixed = F,ignore.case = T, value = T)
###length(filter.tail)
filter.tail <- grep(pattern="F$", x = trust4.fq$CDR3aa, fixed = F,ignore.case = T)
trust4.fq <- trust4.fq[filter.tail, ]

dim4 <- dim(trust4.fq)
print(dim4)

## 5.rm not TRBV
trust4.fq$v.class <- substr(trust4.fq$V,1,4)
trust4.fq <- trust4.fq[trust4.fq$v.class == "TRBV", ]
dim5 <- dim(trust4.fq)
print(dim5)

###optional: plot receptor class
###table(trust4.fq$v.class)
###plot(table(trust4.fq$v.class))

# export filtered file
output.name <- paste(args[2],"/",args[3],"_report_filter.tsv",sep = "")
log.name <- paste(args[2],"/",args[3],"_filter.log",sep = "")
## save filter output
write.table(x = trust4.fq, file = output.name,sep = "\t",row.names = F,quote = F)
## save filter info
trust4.fq.log <- t(data.frame(dim0,dim1,dim2,dim3,dim4,dim5))
write.table(x = trust4.fq.log, file = log.name, sep = "\t",row.names = T,quote = F)
