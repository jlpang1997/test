DELIMITER 
CREATE PROCEDURE demo_in_parameter(IN p_in int)  
    BEGIN   
    SELECT p_in;   
    SET p_in=2;   
    SELECT p_in;   
    END ;


set @p_in=1;
call demo_in_parameter(@p_in);