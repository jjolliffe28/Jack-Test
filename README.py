SUM(IF DATEPART('quarter', [Order Date]) = DATEPART('quarter', TODAY()) THEN [Sales] END) -
SUM(IF DATEPART('quarter', [Order Date]) = DATEPART('quarter', DATEADD('quarter', -1, TODAY())) THEN [Sales] END)


SUM(IF DATEPART('year', [Order Date]) = DATEPART('year', TODAY()) THEN [Sales] END) -
SUM(IF DATEPART('year', [Order Date]) = DATEPART('year', DATEADD('year', -1, TODAY())) THEN [Sales] END)


TOPN(3, 
    {FIXED [Quarter]: SUM(IF DATEDIFF('quarter', [Order Date], TODAY()) = 0, [Commitments], 0)} 
    - {FIXED [Quarter]: SUM(IF DATEDIFF('quarter', [Order Date], TODAY()) = 1, [Commitments], 0)}
    , 1)
