<?php
$conn = mysqli_connect("localhost","root","","id20900224_contact");
if($conn==false){
    die("error".mysqli_connect_error());
}
$name=$_POST["name"];
$email=$_POST["email"];
$msg=$_POST["msg"];
$sql = "INSERT INTO contact(Name,Email,Message) VALUES('$name','$email','$msg');";
if(mysqli_query($conn, $sql)){
    echo "<script>
   alert('Contact Details sent, Harsh will contact you soon');
   window.location.assign('home.html');
   </script>";
    $stmt->close();
    $conn->close();
}
else{
    echo("ERROR: Hush ! Sorry $sql ".mysqli_error($conn));
}
mysqli_close($conn);
?>

