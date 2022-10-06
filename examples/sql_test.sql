/**
 @ingroup examples
 @file

 @brief Voorbeeld SQL
 
 @version 1.0

 @author Arco van Geest <d.a.c.vangeest@tudelft.nl>
 
 @date 20160907 Ageest Eerste versie
  
*/

-- This is an internal comment
--! example documentation
Select * from *;
--! 
--! Empty lines are needed if you want a neq paragraph
--! It is possible to include complete code
--! @verbatim
Select name from users;
--! @endverbatim

GO
CREATE PROCEDURE testDox
--! para nvarchar(50) - zoekterm
	@para nvarchar(50)
AS
	select name where name = @para
GO

-- end