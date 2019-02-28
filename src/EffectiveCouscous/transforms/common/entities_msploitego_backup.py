from canari.maltego.message import *

__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, MSM Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'


class SNMPCommunity(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'sploitego'

    snmp_community = StringEntityField('snmp.community', display_name='SNMP Community', is_value=True)
    snmp_agent = StringEntityField('snmp.agent', display_name='Agent')
    snmp_version = StringEntityField('snmp.version', display_name='SNMP Version')
    ip_port = IntegerEntityField('ip.port', display_name='Port')


class ssl(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ApacheTomcat(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaAccountInformation(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SquidProxyServer(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class compressnet(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class dBase(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Nmap(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class NetworkInterface(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_networkinterface = StringEntityField('properties.networkinterface', display_name='Network Interface', is_value=True)


class Hostname(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_hostname = StringEntityField('properties.hostname', display_name='Hostname', is_value=True)


class IOS(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class wapwsp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class smtp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class XSSVulnerability(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ObjectRequestBroker(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class imap(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ApacheKafka(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class EncryptedPassword(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ApachePHP(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class nginx(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class WebFile(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_webfile = StringEntityField('properties.webfile', display_name='Web File', is_value=True)
    contents = StringEntityField('contents', display_name='Contents')


class UDPPort(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class msdp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class OracleXMLDB(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class PossibleEntryPoint(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'paterva'

    properties_possibleentrypoint = StringEntityField('properties.possibleentrypoint', display_name='PossibleEntryPoint', is_value=True)
    entry = StringEntityField('entry', display_name='Entry')
    type = StringEntityField('type', display_name='Type')
    additional = StringEntityField('additional', display_name='Additional Info')


class nbstatinformation(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Samba(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_samba = StringEntityField('properties.samba', display_name='Samba', is_value=True)


class NmapReport(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'sploitego'

    report = StringEntityField('report', display_name='Nmap Report', is_value=True)
    scan_command = StringEntityField('scan.command', display_name='Nmap Command')
    report_file = StringEntityField('report.file', display_name='Report File')


class Windows7(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ClosedPort(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ipp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ansys(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class NessusReport(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'sploitego'

    name = StringEntityField('name', display_name='Nessus Report', is_value=True)


class SambaService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class EmbeddedOS(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Service(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'sploitego'

    servicename = StringEntityField('servicename', display_name='Service', is_value=True)
    ip_destination = StringEntityField('ip.destination', display_name='Destination IP')
    protocol = StringEntityField('protocol', display_name='Protocol')
    port = StringEntityField('port', display_name='Port')


class WebURL(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_weburl = StringEntityField('properties.weburl', display_name='Web URL', is_value=True)


class AdvancedMultithreadedServer(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class CiscoVPN(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class FTPVulnerability(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Solaris(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Hacked(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class backorifice(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class FileContents(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SiteCategory(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'sploitego'

    properties_sitecategory = StringEntityField('properties.sitecategory', display_name='Site Category', is_value=True)


class ssdp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Fingerprint(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'oscp'

    oscp_fingerprint = StringEntityField('oscp.fingerprint', display_name='Fingerprint', is_value=True)


class rdp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaServer(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class X11(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class NessusVulnerability(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'sploitego'

    vulnerability = StringEntityField('vulnerability', display_name='Nessus Vulnerability', is_value=True)


class nfsacl(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SiteURL(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_siteurl = StringEntityField('properties.siteurl', display_name='Site URL', is_value=True)


class GoAheadWebServer(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaFile(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_sambafile = StringEntityField('properties.sambafile', display_name='Samba File', is_value=True)


class MetasploitLoot(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_metasploitloot = StringEntityField('properties.metasploitloot', display_name='Metasploit Loot [from postgres DB]', is_value=True)


class UserGroup(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_usergroup = StringEntityField('properties.usergroup', display_name='User Group', is_value=True)


class natpmp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class IISWebservice(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class irc(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Checked(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class AdobeserverService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class AFS(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Password(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'haveibeenpwned'

    properties_password = StringEntityField('properties.password', display_name='Password', is_value=True)
    password = StringEntityField('password', display_name='Password')


class SambaShareInformation(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SotwareComponents(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_sotwarecomponents = StringEntityField('properties.sotwarecomponents', display_name='Sotware Components', is_value=True)


class SambaPasswordPolicyInfo(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class RoutingIP(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class DNSInformation(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class WAF(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SNMP(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SIP(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class CSFR(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_csrfvulnerability = StringEntityField('properties.csrfvulnerability', display_name='CSRF Vulnerability', is_value=True)


class ApacheVulnerability(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class blackjack(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class msdtc(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class RocketWebServer(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaOSInformation(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class vnc(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class MetasploitService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_metasploitservice = StringEntityField('properties.metasploitservice', display_name='Metasploit Service', is_value=True)
    info = StringEntityField('info', display_name='Info')
    name = StringEntityField('name', display_name='Name')
    proto = StringEntityField('proto', display_name='Protocol')
    hostid = StringEntityField('hostid', display_name='Host ID')


class SSHAuthenticationMethod(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_sshauthenticationmethod = StringEntityField('properties.sshauthenticationmethod', display_name='SSH Authentication Method', is_value=True)


class directplaysrvr(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class FreeBSD(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class mssql(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class RDPVulnerability(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class CommuniDatePro(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class OracleHTTPServer(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Nodejs(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class epmap(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class tcpwrapped(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class MeterpreterSession(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_meterpretersession = StringEntityField('properties.meterpretersession', display_name='Meterpreter Session', is_value=True)


class LinuxOperatingSystem(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Landesk(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class MSExchangeLogCopier(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class fmtp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class KeyServer(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaShare(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class lighttpd(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SourceCodeComment(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_sourcecodecomment = StringEntityField('properties.sourcecodecomment', display_name='Source Code Comment', is_value=True)


class MetasploitSession(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'sploitego'

    metasploit_session = StringEntityField('metasploit.session', display_name='Metasploit Session', is_value=True)


class Process(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class AccessDenied(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_accessdenied = StringEntityField('properties.accessdenied', display_name='Access Denied', is_value=True)


class WebService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class NAS(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class kerberos(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class xmpp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaVulnerability(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class mysql(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class WindowsXP(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class boinc(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class IsVulnerable(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class MetasploitWorkspace(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_metasploitworkspace = StringEntityField('properties.metasploitworkspace', display_name='Metasploit Workspace', is_value=True)


class bakbonenetvault(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class LDAP(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class OperatingSystem(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_operatingsystem = StringEntityField('properties.operatingsystem', display_name='Operating System', is_value=True)


class JavaRMI(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class breach(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'haveibeenpwned'

    properties_breach = StringEntityField('properties.breach', display_name='Breach', is_value=True)


class NetworkService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'yourorganization'



class wfremotertm(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ServerInfo(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'oscp'

    oscp_servername = StringEntityField('oscp.servername', display_name='Server Name', is_value=True)


class cifs(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class FalsePositive(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_falsepositive = StringEntityField('properties.falsepositive', display_name='False Positive', is_value=True)


class SSHService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SessionDetail(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_sessiondetail = StringEntityField('properties.sessiondetail', display_name='Session Detail', is_value=True)


class HTTPFileServer(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class PossibleInjectionPoint(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'paterva'

    properties_possibleinjectionpoint = StringEntityField('properties.possibleinjectionpoint', display_name='Possible Injection Point', is_value=True)
    url = StringEntityField('url', display_name='None')
    method = StringEntityField('method', display_name='None')
    postdata = StringEntityField('postdata', display_name='None')
    haschecked = BooleanEntityField('haschecked', display_name='None')
    varstocheck = StringEntityField('varstocheck', display_name='None')
    db_guess = StringEntityField('db_guess', display_name='None')


class Jetty(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaUser(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class DNSService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Oracle(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Port(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'sploitego'

    port = IntegerEntityField('port', display_name='Port', is_value=True)
    ip_source = StringEntityField('ip.source', display_name='Source IP')
    ip_destination = StringEntityField('ip.destination', display_name='Destination IP')
    protocol = StringEntityField('protocol', display_name='Protocol')
    port_response = StringEntityField('port.response', display_name='Port Response')
    port_status = StringEntityField('port.status', display_name='Port Status')


class WindowsMasterBrowser(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_windowsmasterbrowser = StringEntityField('properties.windowsmasterbrowser', display_name='Windows Master Browser', is_value=True)


class MetasploitDbXMLFile(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Webmin(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Windows2012(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class DHCP(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class WebForm(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_webform = StringEntityField('properties.webform', display_name='Web Form', is_value=True)


class Credentials(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_credentials = StringEntityField('properties.credentials', display_name='Credentials', is_value=True)


class pop3(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaMachineEnumeration(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class DiskstationManager(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class CISCO(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class NetworkService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class MicrosoftHTTPAPI(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Windows2000(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Windows2003(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class MicrosoftTerminalServices(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class NetworkShare(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class WordpressInfo(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_wordpressinfo = StringEntityField('properties.wordpressinfo', display_name='Wordpress Info', is_value=True)


class finger(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ntp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ident(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ftp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class ajp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class SambaGroupInformation(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Windows2008(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class winrm(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Apachehttpd(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class chargen(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class httpsecureheaders(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_httpsecurityheader = StringEntityField('properties.httpsecurityheader', display_name='HTTP Security Header', is_value=True)


class MetasploitModule(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_metasploitmodule = StringEntityField('properties.metasploitmodule', display_name='Metasploit Module', is_value=True)


class Bacnet(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class WebDirectoryInfo(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class RPC(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class RPCoverhttp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class LootFile(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_lootfile = StringEntityField('properties.lootfile', display_name='Loot File', is_value=True)


class ExploitDBItem(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_exploitdbitem = StringEntityField('properties.exploitdbitem', display_name='Exploit DB Item', is_value=True)


class PostgresqlDB(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_postgresqldb = StringEntityField('properties.postgresqldb', display_name='Postgresql DB', is_value=True)
    user = StringEntityField('user', display_name='None')
    password = StringEntityField('password', display_name='None')


class OHost(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'oscp'

    oscp_source = StringEntityField('oscp.source', display_name='OSCP Host', is_value=True)


class rtsp(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Lansource(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class WindowsOperatingSystem(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class niktodetail(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_niktodetail = StringEntityField('properties.niktodetail', display_name='Nikto Detail', is_value=True)


class RelevantInformation(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'

    properties_relevantinformation = StringEntityField('properties.relevantinformation', display_name='Relevant Information', is_value=True)


class telnet(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class PotentialBackdoor(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class llmnr(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class Password(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'msploitego'



class AS(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    number = IntegerEntityField('as.number', display_name='AS Number')


class Affiliation(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class Alias(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    alias = StringEntityField('properties.alias', display_name='Alias')


class Banner(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    text = StringEntityField('banner.text', display_name='Banner')


class Bebo(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class BuiltWithRelationship(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'maltego'

    matches = StringEntityField('matches', display_name='Matches')
    builtwith = StringEntityField('properties.builtwithrelationship', display_name='BuiltWith Technology')


class BuiltWithTechnology(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'maltego'

    builtwith = StringEntityField('properties.builtwithtechnology', display_name='BuiltWith Technology')


class CircularArea(Entity):
    _category_ = 'Locations'
    _namespace_ = 'maltego'

    radius = IntegerEntityField('radius', display_name='Radius (m)')
    longitude = FloatEntityField('longitude', display_name='Longitude')
    latitude = FloatEntityField('latitude', display_name='Latitude')
    area_circular = StringEntityField('area.circular', display_name='Circular Area')


class Company(Entity):
    _category_ = 'Groups'
    _namespace_ = 'maltego'

    name = StringEntityField('title', display_name='Name')


class DNSName(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    fqdn = StringEntityField('fqdn', display_name='DNS Name')


class Device(Entity):
    _category_ = 'Devices'
    _namespace_ = 'maltego'

    device = StringEntityField('properties.device', display_name='Device')


class Document(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    url = StringEntityField('url', display_name='URL')
    title = StringEntityField('title', display_name='Title')
    metadata = StringEntityField('document.metadata', display_name='Meta-Data')


class Domain(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    whois_info = StringEntityField('whois-info', display_name='WHOIS Info')
    fqdn = StringEntityField('fqdn', display_name='Domain Name')


class EmailAddress(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    email = StringEntityField('email', display_name='Email Address')


class Facebook(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class FacebookObject(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego'

    object = StringEntityField('properties.facebookobject', display_name='Facebook Object')


class File(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    source = StringEntityField('source', display_name='Source')
    description = StringEntityField('description', display_name='Description')


class Flickr(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class GPS(Entity):
    _category_ = 'Locations'
    _namespace_ = 'maltego'

    longitude = FloatEntityField('longitude', display_name='Longitude')
    latitude = FloatEntityField('latitude', display_name='Latitude')
    gps = StringEntityField('properties.gps', display_name='GPS Co-ordinate')


class Hash(Entity):
    _category_ = 'Malware'
    _namespace_ = 'maltego'

    owner = StringEntityField('owner', display_name='Owner')
    included_media_types = StringEntityField('includeMediaType', display_name='Included Media Types')
    hash = StringEntityField('properties.hash', display_name='Hash')
    excluded_media_types = StringEntityField('excludeMediaType', display_name='Excluded Media Types')
    before = DateEntityField('before', display_name='Before')
    after = DateEntityField('after', display_name='After')


class Hashtag(Entity):
    _category_ = 'Social'
    _namespace_ = 'maltego'

    hashtag = StringEntityField('twitter.hashtag', display_name='Hashtag')


class IPv4Address(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    ipv4address = StringEntityField('ipv4-address', display_name='IP Address')
    internal = BooleanEntityField('ipaddress.internal', display_name='Internal')


class Image(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    url = StringEntityField('fullImage', display_name='URL')
    description = StringEntityField('properties.image', display_name='Description')


class Linkedin(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class LinuxOperatingSystem(Entity):
    _category_ = 'Operating Systems'
    _namespace_ = 'metasploit'



class Location(Entity):
    _category_ = 'Locations'
    _namespace_ = 'maltego'

    streetaddress = StringEntityField('streetaddress', display_name='Street Address')
    name = StringEntityField('location.name', display_name='Name')
    longitude = FloatEntityField('longitude', display_name='Longitude')
    latitude = FloatEntityField('latitude', display_name='Latitude')
    countrycode = StringEntityField('countrycode', display_name='Country Code')
    country = StringEntityField('country', display_name='Country')
    city = StringEntityField('city', display_name='City')
    areacode = StringEntityField('location.areacode', display_name='Area Code')
    area = StringEntityField('location.area', display_name='Area')


class MXRecord(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    priority = IntegerEntityField('mxrecord.priority', display_name='Priority')
    fqdn = StringEntityField('fqdn', display_name='DNS Name')


class MetasploitService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'metasploit'

    serviceid = StringEntityField('serviceid', display_name='Service ID')
    proto = StringEntityField('proto', display_name='Protocol')
    name = StringEntityField('name', display_name='Name')
    info = StringEntityField('info', display_name='Info')
    hostid = StringEntityField('hostid', display_name='Host ID')


class MsfEntity(Entity):
    _category_ = 'None'
    _namespace_ = 'metasploit'



class MySpace(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class NSRecord(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    fqdn = StringEntityField('fqdn', display_name='DNS Name')


class Netblock(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    ipv4range = StringEntityField('ipv4-range', display_name='IP Range')


class NominatimLocation(Entity):
    _category_ = 'Locations'
    _namespace_ = 'maltego'

    nominatim = StringEntityField('properties.nominatimlocation', display_name='Nominatim Location')


class Organization(Entity):
    _category_ = 'Groups'
    _namespace_ = 'maltego'

    name = StringEntityField('title', display_name='Name')


class Orkut(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class Person(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    lastname = StringEntityField('person.lastname', display_name='Surname')
    fullname = StringEntityField('person.fullname', display_name='Full Name')
    firstnames = StringEntityField('person.firstnames', display_name='First Names')


class PhoneNumber(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    phonenumber = StringEntityField('phonenumber', display_name='Phone Number')
    lastnumbers = StringEntityField('phonenumber.lastnumbers', display_name='Last Digits')
    countrycode = StringEntityField('phonenumber.countrycode', display_name='Country Code')
    citycode = StringEntityField('phonenumber.citycode', display_name='City Code')
    areacode = StringEntityField('phonenumber.areacode', display_name='Area Code')


class Phrase(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    text = StringEntityField('text', display_name='Text')


class Port(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    number = StringEntityField('port.number', display_name='Ports')


class Sentiment(Entity):
    _category_ = 'Personal'
    _namespace_ = 'maltego'

    sentiment = StringEntityField('properties.sentiment', display_name='Sentiment')


class Service(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    ports = StringEntityField('port.number', display_name='Ports')
    name = StringEntityField('service.name', display_name='Description')
    banner = StringEntityField('banner.text', display_name='Service Banner')


class Spock(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    websites = StringEntityField('spock.websites', display_name='Listed Websites')
    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class TrackingCode(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    unique_identifier = StringEntityField('properties.uniqueidentifier', display_name='Uniqueidentifier')
    identifier_type = StringEntityField('identifierType', display_name='Identifier Type')


class Tweet(Entity):
    _category_ = 'None'
    _namespace_ = 'maltego'

    tweet_id = StringEntityField('id', display_name='Tweet ID')
    tweet = StringEntityField('twit.name', display_name='Tweet')
    title = StringEntityField('title', display_name='Title')
    image_link = StringEntityField('imglink', display_name='Image Link')
    date_published = StringEntityField('pubdate', display_name='Date published')
    content = StringEntityField('content', display_name='Content')
    author_uri = StringEntityField('author_uri', display_name='Author URI')
    author = StringEntityField('author', display_name='Author')


class Twit(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego'

    title = StringEntityField('title', display_name='Title')
    pubdate = StringEntityField('pubdate', display_name='Date published')
    name = StringEntityField('twit.name', display_name='Twit')
    img_link = StringEntityField('img_link', display_name='Image Link')
    id = StringEntityField('id', display_name='Twit ID')
    content = StringEntityField('content', display_name='Content')
    author_uri = StringEntityField('author_uri', display_name='Author URI')
    author = StringEntityField('author', display_name='Author')


class Twitter(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    screenname = StringEntityField('twitter.screen-name', display_name='Screen Name')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    number = IntegerEntityField('twitter.number', display_name='Twitter Number')
    network = StringEntityField('affiliation.network', display_name='Network')
    fullname = StringEntityField('person.fullname', display_name='Real Name')
    friendcount = IntegerEntityField('twitter.friendcount', display_name='Friend Count')


class TwitterUserList(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego'

    uri = StringEntityField('twitter.list.uri', display_name='URI')
    subscriber_count = StringEntityField('twitter.list.subscribers', display_name='Subscriber Count')
    slug = StringEntityField('twitter.list.slug', display_name='Slug')
    name = StringEntityField('twitter.list.name', display_name='Name')
    member_count = StringEntityField('twitter.list.members', display_name='Member Count')
    id_ = StringEntityField('twitter.list.id', display_name='ID')
    full_name = StringEntityField('twitter.list.fullname', display_name='Full Name')
    description = StringEntityField('twitter.list.description', display_name='Description')


class URL(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    url = StringEntityField('url', display_name='URL')
    title = StringEntityField('title', display_name='Title')
    short_title = StringEntityField('short-title', display_name='Short title')


class Unknown(Entity):
    _category_ = 'Unknown'
    _namespace_ = 'canari'



class Vulnerability(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'maltego'

    id = StringEntityField('vulnerability.id', display_name='ID')


class WebTitle(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    title = StringEntityField('title', display_name='Title')


class Webdir(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    name = StringEntityField('directory.name', display_name='Name')


class Website(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    ssl_enabled = BooleanEntityField('website.ssl-enabled', display_name='SSL Enabled')
    ports = IntegerEntityField('ports', display_name='Ports')
    fqdn = StringEntityField('fqdn', display_name='Website')


class WikiEdit(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')


class Windows2000(Entity):
    _category_ = 'Operating Systems'
    _namespace_ = 'metasploit'



class Windows2003(Entity):
    _category_ = 'Operating Systems'
    _namespace_ = 'metasploit'



class Windows2012(Entity):
    _category_ = 'Operating Systems'
    _namespace_ = 'metasploit'



class Windows7(Entity):
    _category_ = 'Operating Systems'
    _namespace_ = 'metasploit'



class WindowsXP(Entity):
    _category_ = 'Operating Systems'
    _namespace_ = 'metasploit'



class Zoominfo(Entity):
    _category_ = 'Social Network'
    _namespace_ = 'maltego.affiliation'

    uid = StringEntityField('affiliation.uid', display_name='UID')
    profile_url = StringEntityField('affiliation.profile-url', display_name='Profile URL')
    person_name = StringEntityField('person.name', display_name='Name')
    network = StringEntityField('affiliation.network', display_name='Network')

