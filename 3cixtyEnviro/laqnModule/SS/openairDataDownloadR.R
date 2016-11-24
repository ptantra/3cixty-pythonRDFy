install.packages('openair')

library(openair)

KCLmeta <-  importMeta(source = "kcl", all = FALSE)
names(KCLmeta)[5] <- 'site_type'
KCLmeta$geom <- paste("POINT (",KCLmeta$latitude, ",",KCLmeta$longitude,")", sep=" ")
KCLmeta <- KCLmeta[complete.cases(KCLmeta),]

write.csv(KCLmeta  , file = "/Users/patrick/3cixty/IN/Kings/KCLmeta.csv")
