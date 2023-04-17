SUM(IF DATEPART('quarter', [Order Date]) = DATEPART('quarter', TODAY()) THEN [Sales] END) -
SUM(IF DATEPART('quarter', [Order Date]) = DATEPART('quarter', DATEADD('quarter', -1, TODAY())) THEN [Sales] END)


SUM(IF DATEPART('year', [Order Date]) = DATEPART('year', TODAY()) THEN [Sales] END) -
SUM(IF DATEPART('year', [Order Date]) = DATEPART('year', DATEADD('year', -1, TODAY())) THEN [Sales] END)
