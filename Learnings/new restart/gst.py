"""SP:selling price  cgst:<central govt. gst>  sgst:<state govt. gst>"""
item=input("Enter Item name:")
SP=float(input("Enter the selling price of item " +item+ ":"))
gstRate=float(input("ENter the GST rates(%):"))
cgst=SP*((gstRate/2)/100)
sgst=cgst
amount=SP+cgst+sgst   #coustomers will buy at this price
print("\t INVOICE")
print("\t\titems:",item)
print("\t\tPrice:",SP)
print("\t\tCGST(@",(gstRate/2),"%):",cgst)
print("\t\tSGST(@",(gstRate/2),"%):",sgst)
print("\t\tAmount Payable:",amount)
