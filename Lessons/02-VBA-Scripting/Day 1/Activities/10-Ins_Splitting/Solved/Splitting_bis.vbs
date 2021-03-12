Sub SimpleArrays():
    
    ' String Splitting Example
    ' ------------------------------------------
    Dim Words() As String
    Dim Shakespeare As String
    Shakespeare = Range("A1").Value

    Dim index as Integer
    index = Range("A2").Value

    ' Break apart the Shakespeare quote into individual words
    Words = Split(Shakespeare, " ")

    ' Print individual word
    Range("A3").Value = Words(index)

End Sub
