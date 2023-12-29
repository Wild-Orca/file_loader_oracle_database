  -- Create or replace a non-editionable procedure named prc_export_archives
  create or replace noneditionable procedure prc_export_archives as
  -- Set the pre-defined directory object where you want to export the files
  v_export_dir varchar2(200) := 'EXPORT_DIR'; -- Replace 'EXPORT_DIR' with your pre-defined directory name

  -- Define the local directory path for exporting files
  v_directory_path varchar2(4000) := 'your_directory';

  -- Declare a variable to store the count of existing directories with the given name
  v_directory_count number;

  -- Cursor variables to fetch records from the tb_test table
  cursor file_cursor is
    select file_name
          ,file_extension
          ,file_content_blob
          ,file_content_clob
      from tb_test;

  -- File variables for handling file operations
  v_file      utl_file.file_type;
  v_file_path varchar2(200);
  v_buffer    varchar2(32767);
begin
  -- Check if the directory already exists
  select count(*)
    into v_directory_count
    from all_directories
   where directory_name = v_export_dir;

  -- If the directory doesn't exist, create it dynamically
  if v_directory_count = 0 then
    execute immediate 'CREATE DIRECTORY ' || v_export_dir || ' AS ''' || v_directory_path || '''';
  end if;

  -- Loop through the records in the tb_test table
  for file_record in file_cursor loop
    -- Construct the full file path with platform-dependent directory separator
    v_file_path := v_export_dir || '\' || file_record.file_name || file_record.file_extension;
  
    -- Open the file for writing and write the file content to the file
    if file_record.file_content_blob is not null then
      v_file := utl_file.fopen(v_export_dir, file_record.file_name || file_record.file_extension, 'wb');
      utl_file.put_raw(v_file, file_record.file_content_blob);
    elsif file_record.file_content_clob is not null then
      v_file := utl_file.fopen(v_export_dir, file_record.file_name || file_record.file_extension, 'w', v_buffer);
      utl_file.put(v_file, file_record.file_content_clob);
    end if;
  
    -- Close the file
    utl_file.fclose(v_file);
  
    -- Display a message for each exported file
    dbms_output.put_line('Exported: ' || v_file_path);
  end loop;

  -- Display a final message
  dbms_output.put_line('Export process completed.');

exception
  -- Exception handling block
  when others then
    -- Handle exceptions (customize as needed)
    dbms_output.put_line('Error: ' || sqlerrm);
end prc_export_archives;
/