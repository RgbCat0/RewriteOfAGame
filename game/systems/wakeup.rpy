# Shared by the room entry and wakeup router so their conditions cannot drift.
init python:
    def special_wakeup_target():
        if whereami != "playerRoom" or timeofday != "Morning":
            return None
        if amountspent >= 350 and ashleychecker == 0 and watchcount == 0:
            return "ashleyinteraction1part1"
        if miaphase2interaction2 == 4 and currentchapter == 3 and dayNumber > 21:
            return "miaphase3interaction1part1"
        if miaphase1interaction2 == 4:
            return "miaphase1interaction2part3wakeup"
        if avaphase2interaction1 == 1 and avadaycheck < dayNumber:
            return "avaphase2interaction2part1"
        if charlottephase2interaction2 == 2:
            return "charlottephase2interaction2part1"
        return None
