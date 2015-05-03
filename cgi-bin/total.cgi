#!/usr/bin/perl -wT
 
use CGI;
use CGI::Carp qw(fatalsToBrowser);
 
use strict;
use warnings;
use File::Basename;
require "/home/jiangbo/public_html/cgi-bin/ch09/validate_email_address_sub.lib";



# Clean up environment for taint mode before calling sendmail
BEGIN {
    $ENV{PATH} = "/bin:/usr/bin";
    delete @ENV{ qw( IFS CDPATH ENV BASH_ENV ) };
}

my $q       = new CGI;
my $email   = &validate_email_address( $q->param( "email" ) );
my $message = $q->param( "message" );
my $txt = $q->param( "fname" );
my $lname = $q->param( "lname" );
my $month = $q->param( "month" );
my $date = $q->param( "date" );
my $year = $q->param( "year" );
my $sex = $q->param( "sex" );
my $line1 = $q->param( "line1" );
my $line2 = $q->param( "line2" );
my $city = $q->param( "city" );
my $State = $q->param( "State" );
my $pin = $q->param( "pin" );
my $countries = $q->param( "countries" );
my $list2 = $q->param( "list2" );
my $major = $q->param( "major" );
my $cityindia = $q->param( "cityindia" );
my $stateindia = $q->param( "stateindia" );

unless ( $email ) {
    print $q->header( "text/html" ),
          $q->start_html( "Invalid Email Address" ),
          $q->h1( "Invalid Email Address" ),
          $q->p( "The email address you entered is invalid. " .
                 "Please use your browserÕs Back button to " .
                 "return to the form and try again." );
          $q->end_html;
    exit;
}

send_feedback( $email, $message, $txt, $lname, $month, $date, $year, $sex, $line1, $line2, $city, $State, $pin, $countries, $list2, $major, $cityindia, $stateindia);




sub send_feedback {
    my( $email, $message, $txt, $lname, $month, $date, $year, $sex, $line1, $line2, $city, $State, $pin, $countries,$list2, $major, $cityindia, $stateindia) = @_;
    
    open MAIL, "| /usr/lib/sendmail -t -i"
        or die "Could not open sendmail: $!";
    
    print MAIL <<END_OF_MESSAGE;
#To: ISA\@bradley.edu
To: $email
Reply-To: $email
Subject: Confirmation

Feedback from a user:

Your Message :$message
Your Name : $txt $lname
Your Date of BIRTH : $month/$date/$year
Sex : $sex
Address : $line1, $line2, $city, $State, $pin, $countries
You are : $list2
Your India Address is : $cityindia, $stateindia



END_OF_MESSAGE
    close MAIL or die "Error closing sendmail: $!";
}

sub send_receipt {
    my $email       = shift;
    #my $from_email  = shift || $ENV{SERVER_ADMIN};
    my $from_email  = shift || "ISA\@cs1.bradley.edu";
    my $from_name   = shift || "ISA";
 
    open MAIL, "| /usr/lib/sendmail -t -F '$from_name' -f '$from_email'"
        or die "Could not open sendmail: $!";
    print MAIL <<END_OF_MESSAGE;
To: $email
Subject: Confirmation Message

Your Information is saved Successfully!
END_OF_MESSAGE
    close MAIL or die "Error closing sendmail: $!";
}


$CGI::POST_MAX = 1024 * 5000; #adjust as needed (1024 * 5000 = 5MB)
$CGI::DISABLE_UPLOADS = 0; #1 disables uploads, 0 enables uploads
 
my $query = CGI->new;
 
unless ($CGI::VERSION >= 2.47) { 
   error('Your version of CGI.pm is too old. You must have verison 2.47 or higher to use this script.')
}
 
my $upload_dir = '/home/ashrivastava2/public_html/upload';
 
# a list of valid characters that can be in filenames
my $filename_characters = 'a-zA-Z0-9_.-';
 
my $file = $query->param("photo") or error('No file selected for upload.') ;
my $email_address = $query->param("email") || 'Annonymous';
 
# get the filename and the file extension
# this could be used to filter out unwanted filetypes
# see the File::Basename documentation for details
my ($filename,undef,$ext) = fileparse($file,qr{\..*});
 
# append extension to filename
$filename .= $ext;
 
# convert spaces to underscores "_"
$filename =~ tr/ /_/;
 
# remove illegal characters
$filename =~ s/[^$filename_characters]//g;
 
# satisfy taint checking
if ($filename =~ /^([$filename_characters]+)$/) {
   $filename = $1;
}
else{
   error("The filename is not valid. Filenames can only contain these characters: $filename_characters")
}
 
# this is very crude but validating an email address is not an easy task
# and is beyond the scope of this article. To validate an email
# address properly use the Email::Valid module. I do not include
# it here because it is not a core module.
unless ($email_address =~ /^[\w@.-]+$/ && length $email_address < 250) {
   error("The email address appears invalid or contains too many characters. Limit is 250 characters.")
}    
 
my $upload_filehandle = $query->upload("photo");
open (UPLOADFILE, ">$upload_dir/$filename") or error($!);
binmode UPLOADFILE;
while ( <$upload_filehandle> ) {
   print UPLOADFILE;
}
close UPLOADFILE;
 
my $file = '/home/ashrivastava2/public_html/cgi-bin/sign/record.txt';
 
my $q = new CGI;
 
if ($q->request_method() eq 'POST') {
    my $txt = $q->param("fname");
	my $lname = $q->param("lname");
	my $month = $q->param( "month" );
	my $date = $q->param( "date" );
	my $year = $q->param( "year" );
	my $sex = $q->param( "sex" );
	my $line1 = $q->param( "line1" );
	my $line2 = $q->param( "line2" );
	my $city = $q->param( "city" );
	my $State = $q->param( "State" );
	my $pin = $q->param( "pin" );
	my $countries = $q->param( "countries" );
	my $list2 = $q->param( "list2" );
	my $major = $q->param( "major" );
	my $cityindia = $q->param( "cityindia" );
	my $stateindia = $q->param( "stateindia" );
	
    open my $fh, '>', $file or die "can't open $file: $!";
    print $fh $txt;
	print $fh $lname;
	print $fh $month;
	print $fh $date;
	print $fh $year;
	print $fh $sex;
	print $fh $line1;
	print $fh $line2;
	print $fh $city;
	print $fh $State;
	print $fh $pin;
	print $fh $countries;
	print $fh $list2;
	print $fh $major;
	print $fh $cityindia;
	print $fh $stateindia;
    close $fh;
    
	print $q->header(),
      $q->start_html(-title=>'Register Successful'),
	  $q->p("Your fname : $txt"),
	  $q->p("Your lname : $lname"),
	  $q->p("Your Date of BIRTH : $month/$date/$year"),
	  $q->p("You are : $sex"),
	  $q->p("Your Address : $line1, $line2, $city, $State, $pin, $countries"),
	  $q->p("You are : $list2"),
	  $q->p("Your major's in : $major"),
	  $q->p("You came from : $cityindia, $stateindia, INDIA"),
	  $q->p("Your photo $filename:"),
	  $q->p("You have registered SUCCESSFULLY...!!"),
      $q->img({src=>"http://cs1.bradley.edu/~ashrivastava2/upload/$filename",alt=>''}),
	   $q->end_html;
    print <<"END_HTML";

END_HTML
    exit;
}
